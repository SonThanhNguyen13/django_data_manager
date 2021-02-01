import os
import json
import random
from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.core import serializers
from . import forms
from . import queries
from django.views import View
from .check_permission import has_permission, return_url_name, check_local_ip, get_client_ip


class DataCategoryView(LoginRequiredMixin, View):
    login_url = '/login/'
    form_class = forms.DataCategoryForm

    def get(self, request):
        """get all data categories"""
        # get form
        form = self.form_class()
        # get all data category & pagination
        data_category = queries.get_all_data_category(reverse=True)
        paginator = Paginator(data_category, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "data_manager_app/dataCategory.html",
                      {"form": form, "datas": page_obj})

    def post(self, request):
        """add data category"""
        # check permission
        url_name = return_url_name(request.path)
        if not has_permission(request.user.role_id, url_name, request.method):
            return JsonResponse({"error": "No permission"}, status=400)
        # get request, check is ajax
        if request.is_ajax:
            form = self.form_class(request.POST)
            if form.is_valid():
                instance = form.save()
                # send to client side.
                return JsonResponse({"Add data": instance.name}, status=200)
            else:
                str_error = ''
                for field, errors in form.errors.items():
                    str_error += field + ": "
                    for error in errors:
                        str_error += error + ', '
                return JsonResponse({"error": str_error[:-2]}, status=400)

        return JsonResponse({"error": "Something went terribly wrong"}, status=400)


class EditDataCategory(LoginRequiredMixin, View):
    """Edit data category, post only """
    login_url = '/login/'
    form_class = forms.DataCategoryForm

    def post(self, request, pk):
        # check permission
        url_name = return_url_name(request.path)
        if not has_permission(request.user.role_id, url_name, request.method):
            return JsonResponse({"error": "No permission"}, status=400)
        if request.is_ajax:
            # get data_category by id
            update_data = queries.get_data_category_by_filter(data_category_id=pk)
            form = self.form_class(request.POST, instance=update_data)
            if form.is_valid():
                instance = form.save()
                ser_instance = serializers.serialize('json', [instance, ])
                # send to client side.
                return JsonResponse({"Edit data": {"instance": ser_instance}}, status=200)
            else:
                str_error = ''
                for field, errors in form.errors.items():
                    str_error += field + ": "
                    for error in errors:
                        str_error += error + ', '
                return JsonResponse({"error": str_error[:-2]}, status=400)
        return JsonResponse({"error": "Something went terribly wrong"}, status=400)


class DataPage(LoginRequiredMixin, View):
    """
    View for data page
    """
    login_url = '/login/'
    form_class = forms.DataForm
    form_search = forms.DataFilterForm

    def get(self, request):
        form = self.form_class
        # get data id, name, image
        datas = queries.get_all_data(reverse=True).only("data_id", "name", "data_avatar")
        paginator = Paginator(datas, 30)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(
            request,
            "data_manager_app/data.html",
            {
                "form": form,
                "datas": page_obj,
                "search_form": self.form_search,
            }
        )

    def post(self, request):
        """Create data"""
        url_name = return_url_name(request.path)
        if not has_permission(request.user.role_id, url_name, request.method):
            return JsonResponse({"error": "No permission"}, status=400)
        if request.is_ajax:
            form = self.form_class(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.data_owner = request.user
                instance.save()
                # send to client side.
                return JsonResponse({'instance': instance.name}, status=200)
            else:
                str_error = ''
                for field, errors in form.errors.items():
                    str_error += field + ": "
                    for error in errors:
                        str_error += error + ', '
                return JsonResponse({"error": str_error[:-2]}, status=400)

        return JsonResponse({"error": "Something went terribly wrong"}, status=400)


class SearchData(LoginRequiredMixin, View):
    form_class = forms.DataForm
    form_search = forms.DataFilterForm

    def get(self, request):
        query = {}
        name = request.GET.get('name')
        self.add_to_query(query, "name", name)
        data_category = request.GET.get('data_category')
        self.add_to_query(query, "data_category", data_category)
        size_on_disk = request.GET.get('size_on_disk')
        self.add_to_query(query, "size_on_disk", size_on_disk)
        directory_of_data = request.GET.get('directory_of_data')
        self.add_to_query(query, "directory_of_data", directory_of_data)
        number_of_images = request.GET.get('number_of_images')
        self.add_to_query(query, "number_of_images", number_of_images)
        number_of_classes = request.GET.get('number_of_classes')
        self.add_to_query(query, "number_of_classes", number_of_classes)
        data_owner = request.GET.get('data_owner')
        self.add_to_query(query, 'data_owner', data_owner)
        analyzed = request.GET.get('analyzed')
        if analyzed == 'on':
            self.add_to_query(query, "analyzed", True)
        best_result = request.GET.get('best_result')
        self.add_to_query(query, "best_result", best_result)
        best_analyzed_model = request.GET.get('best_analyzed_model')
        self.add_to_query(query, "best_analyzed_model", best_analyzed_model)
        if len(query) < 1:
            return redirect('/data/')
        search_data = queries.get_data_by_filter(
            reverse=True, **query
        ).only("data_id", "name", "data_avatar")
        if len(search_data) > 0:
            paginator = Paginator(search_data, 30)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(
                request,
                "data_manager_app/data.html",
                {
                    "form": self.form_class,
                    "datas": page_obj,
                    "search_form": self.form_search,
                }
            )
        else:
            return render(
                request,
                "data_manager_app/data.html",
                {
                    "form": self.form_class,
                    "message": "Not found",
                    "search_form": self.form_search,
                }
            )

    def add_to_query(self, query, key, value):
        if value:
            query[key] = value


class DataDetail(LoginRequiredMixin, View):
    login_url = '/login/'
    form_class = forms.DataForm

    def get(self, request, id):
        """Get data to show"""
        data = queries.get_data_by_id(id)
        if data:
            init_data = {
                'name': data.name,
                'data_category': data.data_category,
                'size_on_disk': data.size_on_disk,
                'number_of_images': data.number_of_images,
                "number_of_classes": data.number_of_classes,
                "directory_of_data": data.directory_of_data,
                "iqa_0": data.iqa_0,
                "iqa_1": data.iqa_1,
                "iqa_2": data.iqa_2,
                "iqa_3": data.iqa_3,
                "iqa_4": data.iqa_4,
                "shape_0": data.shape_0,
                "shape_1": data.shape_1,
                "shape_2": data.shape_2,
                "shape_3": data.shape_3,
                "shape_4": data.shape_4,
                "analyzed": data.analyzed,
                "best_result": data.best_result,
                "best_analyzed_model": data.best_analyzed_model,
            }
            form = self.form_class(initial=init_data)
            return render(request, "data_manager_app/dataDetail.html", {"data": data, "form": form})
        else:
            return HttpResponse("404 not found")

    def post(self, request, id):
        """Update data"""
        url_name = return_url_name(request.path)
        if not has_permission(request.user.role_id, url_name, request.method):
            return JsonResponse({"error": "No permission"}, status=400)
        if request.is_ajax and request.method == "POST":
            update_data = queries.get_data_by_id(id)
            if request.user != update_data.data_owner:
                return JsonResponse({"error": "No permission"}, status=400)
            delete_image = None
            if update_data.data_avatar:
                delete_image = os.path.join("media", str(update_data.data_avatar))
            form = self.form_class(request.POST, request.FILES, instance=update_data)
            if form.is_valid():
                # if update image
                if request.FILES:
                    if delete_image:
                        # if delete_image_exist
                        try:
                            os.remove(delete_image)
                        except FileNotFoundError:
                            pass
                instance = form.save()
                instance = serializers.serialize('json', [instance, ])
                # convert to json to change value of foreign key, null to None and Analyzed to string
                instance = json.loads(instance)
                for key, value in instance[0]["fields"].items():
                    if key == 'data_category':
                        instance[0]["fields"][key] = str(queries.get_data_category_by_filter(
                            data_category_id=instance[0]["fields"][key])
                        )
                    elif key == 'best_analyzed_model':
                        instance[0]["fields"][key] = str(queries.get_ai_model_by_id(id=instance[0]["fields"][key]))
                    elif key == 'analyzed':
                        if not value:
                            instance[0]["fields"][key] = "False"
                        else:
                            instance[0]["fields"][key] = "True"
                    elif value is None:
                        instance[0]["fields"][key] = "None"
                # back to string to send to client
                instance = json.dumps(instance)
                # send to client side.
                return JsonResponse({'instance': instance}, status=200)
            else:
                str_error = ''
                for field, errors in form.errors.items():
                    str_error += field + ": "
                    for error in errors:
                        str_error += error + ', '
                return JsonResponse({"error": str_error[:-2]}, status=400)
        else:
            return JsonResponse({"error": "Something went terribly wrong"}, status=400)

    def delete(self, request, id):
        """delete data"""
        url_name = return_url_name(request.path)
        if not has_permission(request.user.role_id, url_name, request.method):
            return JsonResponse({"error": "No permission"}, status=400)
        elif request.is_ajax:
            delete_data = queries.get_data_by_id(id)
            if request.user != delete_data.data_owner:
                return JsonResponse({"error": "No permission"}, status=400)
            # fix sau khi co du model
            if not delete_data:
                return JsonResponse({"error": "Not found"}, status=400)
            queries.delete_data(delete_data)
            # delete image
            if delete_data.data_avatar:
                delete_image = os.path.join("media", str(delete_data.data_avatar))
                try:
                    os.remove(delete_image)
                except FileNotFoundError:
                    pass
            return JsonResponse({}, status=200)
        else:
            return JsonResponse({"error": "Something went terribly wrong"}, status=400)


class Visualize(LoginRequiredMixin, View):
    login_url = '/login/'
    """ Visualize data """
    def get(self, request):
        all_data = queries.get_all_data().count()
        all_category = queries.get_all_data_category().count()
        data_from_model = queries.get_data_by_analyzed()
        true_analyzed = None
        false_analyzed = None
        for i in data_from_model:
            if i["analyzed"]:
                true_analyzed = i["dcount"]
            else:
                false_analyzed = i["dcount"]
        return render(
            request,
            'data_manager_app/dataVisualize.html',
            {
                'number_of_data': all_data,
                'number_of_category': all_category,
                'true_analyzed': true_analyzed,
                'false_analyzed': false_analyzed
            }
        )


class Chart(LoginRequiredMixin, View):
    """Chart by category with ajax"""
    login_url = '/login/'

    def get(self, request):
        # get all category
        all_category = queries.get_all_data_category()
        # colors
        base_colors = [
            'red', 'orange', '#26E037', 'purple', '#2E251E', 'blue',
            'IndianRed', 'Pink', 'LightSalmon', 'DarkKhaki', 'Fuchsia',
            'Lime', 'Aqua', 'MediumSlateBlue', 'Goldenrod', 'Maroon',
            'DimGray', 'Brown',
        ]
        # labels
        labels = []
        colors = []
        data = []
        # append labels, data and colors
        for i in range(len(all_category)):
            labels.append(all_category[i].name)
            # select count data group by category
            data.append(queries.get_data_by_filter(data_category=all_category[i]).count())
            # no more color? Return to the first
            colors.append(base_colors[i % len(base_colors)])
        # replace colors if last colors == first colors
        if len(colors) > 1:
            if colors[-1] == colors[0]:
                new_colors = base_colors.copy()
                new_colors.remove(colors[-1])
                new_colors.remove(colors[-2])
                colors[-1] = random.choice(new_colors)
        # response to ajax
        return JsonResponse(
            data={
                'labels': labels,
                'data': data,
                'color': colors,
            })


class ChartByAnalyzed(LoginRequiredMixin, View):
    """Chart by analyzed with ajax"""
    login_url = '/login/'

    def get(self, request):
        base_colors = ['red', 'blue']
        labels = []
        data = []
        data_from_model = queries.get_data_by_analyzed()
        for i in data_from_model:
            labels.append(i["analyzed"])
            data.append(i["dcount"])
        return JsonResponse(data={
            'labels': labels,
            'data': data,
            'color': base_colors,
        })
