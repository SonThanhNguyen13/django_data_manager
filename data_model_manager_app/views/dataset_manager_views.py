import os
import json
import random
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.core import serializers
from data_model_manager_app import forms
from data_model_manager_app import queries
from django.views import View
from data_model_manager_app.check_permission import has_permission, return_url_name


class DataCategoryView(LoginRequiredMixin, View):
    login_url = '/login/'
    form_class = forms.DataCategoryForm

    def get(self, request):
        """
        Get all data categories
        :param request:
        :return: HTML page contain all categories
        """
        # get form to add category
        form = self.form_class()
        # get all data category & pagination
        data_category = queries.get_all_data_category(reverse=True)
        paginator = Paginator(data_category, 10)
        # paginator, 10 per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "data_manager_app/dataCategory.html",
                      {"form": form, "datas": page_obj})

    def post(self, request):
        """
        Add category
        :param request:
        :return: Category name if added, otherwise error
        """
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
                # send form's error
                str_error = ''
                for field, errors in form.errors.items():
                    str_error += field + ": "
                    for error in errors:
                        str_error += error + ', '
                return JsonResponse({"error": str_error[:-2]}, status=400)

        return JsonResponse({"error": "Something went terribly wrong"}, status=400)


class EditDataCategory(LoginRequiredMixin, View):
    login_url = '/login/'
    # add form
    form_class = forms.DataCategoryForm

    def post(self, request, pk):
        """
        Update data category
        :param request:
        :param pk: id for update
        :return: updated data if success, error if otherwise
        """
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
                # form's error string
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
    # add form
    form_class = forms.DataForm
    # search form
    form_search = forms.DataFilterForm

    def get(self, request):
        """
        Show all data from Datasets
        :param request:
        :return: HTML page show all datasets
        """
        form = self.form_class
        # get all
        datas = queries.get_all_data(reverse=True)
        # paginator
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
        """
        Create datasets record
        :param request:
        :return: dataset name if created, error if otherwise
        """
        # get url name
        url_name = return_url_name(request.path)
        # check permission
        if not has_permission(request.user.role_id, url_name, request.method):
            return JsonResponse({"error": "No permission"}, status=400)
        # check if request is ajax
        if request.is_ajax:
            # get data from form
            form = self.form_class(request.POST, request.FILES)
            # check valid form
            if form.is_valid():
                instance = form.save(commit=False)
                # set owner = request user
                instance.data_owner = request.user
                instance.save()
                # send to client side.
                return JsonResponse({'instance': instance.name}, status=200)
            else:
                # create error string
                str_error = ''
                for field, errors in form.errors.items():
                    # get all field that error
                    str_error += field + ": "
                    # add all error of that field
                    for error in errors:
                        str_error += error + ', '
                # return to client
                return JsonResponse({"error": str_error[:-2]}, status=400)
        # if request not ajax
        return JsonResponse({"error": "Something went terribly wrong"}, status=400)


class SearchData(LoginRequiredMixin, View):
    # add form
    form_class = forms.DataForm
    # search form
    form_search = forms.DataFilterForm

    def get(self, request):
        """
        Search data
        :param request:
        :return: HTML page contain datasets by filter, error if otherwise
        """
        # get search filter. Filter by anything user input
        filter = {}
        name = request.GET.get('name')
        self.add_to_query(filter, "name", name)
        data_category = request.GET.get('data_category')
        self.add_to_query(filter, "data_category", data_category)
        directory_of_data = request.GET.get('directory_of_data')
        self.add_to_query(filter, "directory_of_data", directory_of_data)
        data_owner = request.GET.get('data_owner')
        self.add_to_query(filter, 'data_owner', data_owner)
        analyzed = request.GET.get('analyzed')
        if analyzed == 'on':
            self.add_to_query(filter, "analyzed", True)
        best_analyzed_model = request.GET.get('best_analyzed_model')
        self.add_to_query(filter, "best_analyzed_model", best_analyzed_model)
        # if not input anything, redirect to data page
        if len(filter) < 1:
            return redirect('/data/')
        search_data = queries.get_data_by_filter(reverse=True, **filter)
        # if exist, paginator
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
        # else return "Not found" message
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

    # add item to query
    def add_to_query(self, filter, key, value):
        """
        :param filter: Filter search from user
        :param key: Python dict key
        :param value:Python dict value
        :return: None
        """
        if value:
            filter[key] = value


class DataDetail(LoginRequiredMixin, View):
    login_url = '/login/'
    form_class = forms.DataForm

    def get(self, request, id):
        """
        Show detail of 1 single record from Dataset table
        :param request:
        :param id: Dataset's id to show
        :return: HTML page with dataset's detail
        """
        data = queries.get_data_by_id(id)
        # init data for form
        if data:
            init_data = {
                'name': data.name,
                'data_category': data.data_category,
                'size_on_disk': data.size_on_disk,
                'number_of_images': data.number_of_images,
                "number_of_classes": data.number_of_classes,
                "directory_of_data": data.directory_of_data,
                "brisque": data.brisque,
                "brightness": data.brightness,
                "sharpness": data.sharpness,
                "iqa_3": data.iqa_3,
                "iqa_4": data.iqa_4,
                "mean_width": data.mean_width,
                "mean_height": data.mean_height,
                "shape_2": data.shape_2,
                "shape_3": data.shape_3,
                "shape_4": data.shape_4,
                "analyzed": data.analyzed,
                "best_result": data.best_result,
                "best_analyzed_model": data.best_analyzed_model,
                "note": data.note
            }
            # call form to render to html, with init data to edit form
            form = self.form_class(initial=init_data)
            return render(request, "data_manager_app/dataDetail.html", {"data": data, "form": form})
        else:
            return redirect('/fun/')

    def post(self, request, id):
        """
        Update singgle dataset's information
        :param request:
        :param id: dataset's id to update
        :return: Updateed data (JSON) if success, Error if otherwise
        """
        url_name = return_url_name(request.path)
        if not has_permission(request.user.role_id, url_name, request.method):
            return JsonResponse({"error": "No permission"}, status=403)
        if request.is_ajax and request.method == "POST":
            update_data = queries.get_data_by_id(id)
            if request.user != update_data.data_owner:
                return JsonResponse({"error": "No permission"}, status=403)
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
                            # delete image
                            os.remove(delete_image)
                        except FileNotFoundError:
                            pass
                # save data
                instance = form.save()
                instance = serializers.serialize('json', [instance, ])
                # convert to json to change value of foreign key
                instance = json.loads(instance)
                # data category: id to category name
                instance[0]["fields"]['data_category'] = str(queries.get_data_category_by_filter(
                    data_category_id=instance[0]["fields"]['data_category'])
                )
                # best_analyzed_model: id to name
                instance[0]["fields"]['best_analyzed_model'] = str(
                    queries.get_ai_model_by_id(id=instance[0]["fields"]['best_analyzed_model'])
                )
                # analyzed: True or False to string "True" or "False"
                if not instance[0]["fields"]['analyzed']:
                    instance[0]["fields"]['analyzed'] = "False"
                else:
                    instance[0]["fields"]['analyzed'] = "True"
                # null to string "None"
                for key, value in instance[0]["fields"].items():
                    if value is None:
                        instance[0]["fields"][key] = "None"
                # back to string to send to client
                instance = json.dumps(instance)
                # send to client side.
                return JsonResponse({'instance': instance}, status=200)
            # send form errors
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
        """
        Delete record from datasets table
        :param request:
        :param id: id to delete
        :return: None if success, otherwise error
        """
        url_name = return_url_name(request.path)
        # check permission
        if not has_permission(request.user.role_id, url_name, request.method):
            return JsonResponse({"error": "No permission"}, status=403)
        # check request is ajax
        elif request.is_ajax:
            # get data by id
            delete_data = queries.get_data_by_id(id)
            # check owner
            if request.user != delete_data.data_owner:
                return JsonResponse({"error": "No permission"}, status=403)
            # not found
            if not delete_data:
                return JsonResponse({"error": "Not found"}, status=400)
            # delete data
            delete_data.delete()
            # delete image
            if delete_data.data_avatar:
                # join path
                delete_image = os.path.join("media", str(delete_data.data_avatar))
                # delete image
                try:
                    os.remove(delete_image)
                except FileNotFoundError:
                    pass
            return JsonResponse({}, status=200)
        else:
            return JsonResponse({"error": "Something went terribly wrong"}, status=400)


class Visualize(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        """
        Dataset visualize page
        :param request:
        :return: HTML page visualize datasets
        """
        # count all data
        all_data = queries.get_all_data().count()
        # count all category
        all_category = queries.get_all_data_category().count()
        # count all data by analyzed (True/ False)
        data_from_model = queries.get_data_by_analyzed()
        # analyzed count
        true_analyzed = None
        # not alalyzed count
        false_analyzed = None
        for i in data_from_model:
            if i["analyzed"]:
                true_analyzed = i["dcount"]
            else:
                false_analyzed = i["dcount"]
        # sum all data size
        all_size = queries.get_sum_data_size()['size_on_disk__sum']
        return render(
            request,
            'data_manager_app/dataVisualize.html',
            {
                'number_of_data': all_data,
                'number_of_category': all_category,
                'true_analyzed': true_analyzed,
                'false_analyzed': false_analyzed,
                'all_size': round(all_size, 2),
            }
        )


class Chart(LoginRequiredMixin, View):
    """Chart by category with ajax"""
    login_url = '/login/'

    def get(self, request):
        """
        Datasets by category chart
        :param request:
        :return: JSON for Datasets by category chart. (Labels, data, color)
        """
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
            cate_data = queries.get_data_by_filter(data_category=all_category[i]).count()
            if cate_data > 0:
                labels.append(all_category[i].name)
            # select count data group by category
                data.append(cate_data)
            # no more color? Return to the first
                colors.append(base_colors[i % len(base_colors)])
        # replace colors if last colors == first colors
        if len(colors) > 1:
            if colors[-1] == colors[0]:
                base_colors.remove(colors[-1])
                base_colors.remove(colors[-2])
                # last color = random color in new base color
                colors[-1] = random.choice(base_colors)
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
        """
        Datasets by Analyzed chart
        :param request:
        :return: JSON for Datasets by Analyzed chart. (Labels, data, color)
        """
        base_colors = ['blue', 'red']
        labels = []
        data = []
        # get total anaylyzed = True and False
        data_from_model = queries.get_data_by_analyzed()
        for i in data_from_model:
            # append labels
            labels.append(i["analyzed"])
            # count analyzed
            data.append(i["dcount"])
        return JsonResponse(data={
            'labels': labels,
            'data': data,
            'color': base_colors,
        })


class ChartBySize(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        """
        Datasets by size_on_disk chart
        :param request:
        :return: JSON for Datasets by size_on_disk chart. (Labels, data, color)
        """
        # get all category
        all_category = queries.get_all_data_category()
        # html colors
        base_colors = [
            '#d73027', '#1a9850', '#f46d43',
            '#fdae61', '#fee08b', '#ffffbf',
            '#d9ef8b', '#a6d96a', '#66bd63',
            '#1a9850', '#a50026', '#006837',
        ]
        # labels
        labels = []
        colors = []
        data = []
        for i in range(len(all_category)):
            # get sum data by category
            sum_cate_data_size = queries.get_sum_data_size_by_category(all_category[i])
            # if sum exist
            if sum_cate_data_size['size_on_disk__sum']:
                # if sum > 9
                if sum_cate_data_size['size_on_disk__sum'] > 0:
                    # append labels( category)
                    labels.append(all_category[i].name)
                    # select count data group by category
                    data.append(round(sum_cate_data_size['size_on_disk__sum'], 2))
                    # append colors from the beginning
                    colors.append(base_colors[i % len(base_colors)])
        # check last color = first color
        if len(colors) > 1:
            if colors[-1] == colors[0]:
                # remove 2 last colors in list in base colors
                base_colors.remove(colors[-1])
                base_colors.remove(colors[-2])
                # last colors = random in new base colors
                colors[-1] = random.choice(base_colors)
        # response to ajax
        return JsonResponse(
            data={
                'labels': labels,
                'data': data,
                'color': colors,
            })


class ChartSizeByDirectory(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        """
        Nothing so far
        :param request:
        :return:
        """
        pass
