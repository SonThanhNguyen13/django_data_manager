from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View
from django.core import serializers
from data_model_manager_app.check_permission import has_permission, return_url_name
from data_model_manager_app import forms
from data_model_manager_app import queries


class ModelTrainData(LoginRequiredMixin, View):
    login_url = '/login/'
    form_class = forms.AddModelTrainData
    search_form = forms.SearchModelTrainData

    def get(self, request):
        """
        Return all data from ModelTrainData
        :param request:
        :return:
        """
        # get all data from model_train_data table
        data = queries.get_all_model_train_data(reverse=True)
        # paginator
        paginator = Paginator(data, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # render
        return render(
            request,
            'data_manager_app/modelTrainData.html',
            {
                'form': self.form_class,
                'datas': page_obj,
                'search_form': self.search_form
            }
        )

    def post(self, request):
        """
        Create record in model_train_data
        :param request:
        :return: Record if created, otherwise error
        """
        url_name = return_url_name(request.path)
        # check permission
        if not has_permission(request.user.role_id, url_name, request.method):
            return JsonResponse({'error': 'No permission'}, status=403)
        # check request is ajax
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                # save record
                instance = form.save(commit=False)
                instance.added_by = request.user
                instance.save()
                # instance to json
                ser_instance = serializers.serialize('json', [instance, ])
                # send to client
                return JsonResponse({'Added data': ser_instance}, status=200)
            else:
                # error: Send form's error
                str_error = ''
                for field, errors in form.errors.items():
                    str_error += field + ": "
                    for error in errors:
                        str_error += error + ', '
                return JsonResponse({"error": str_error[:-2]}, status=400)
        else:
            return JsonResponse({"Error": "Something when terribly wrong"}, status=400)


class ModelTrainDataDetail(LoginRequiredMixin, View):
    login_url = '/login/'
    form_class = forms.AddModelTrainData

    def post(self, request, id):
        """
        Update ModelTrainData record
        :param request:
        :param id: id to update
        :return: Success message update, otherwise error
        """
        url_name = return_url_name(request.path)
        # check permission
        if not has_permission(request.user.role_id, url_name, request.method):
            return JsonResponse({"error": "No permission"}, status=403)
        # check request is ajax
        if request.is_ajax:
            # get update data
            update_data = queries.get_model_train_data_by_id(id)
            # not found
            if not update_data:
                return HttpResponse('404 not found')
            # check if request user is owner
            if request.user != update_data.added_by:
                return JsonResponse({"error": "No permission"}, status=403)
            # get form
            form = self.form_class(request.POST)
            if form.is_valid():
                # update
                instance = form.save(commit=False)
                instance.added_by = request.user
                instance.save()
                # send to client side.
                return JsonResponse({"Edit data": {"instance": "Success"}}, status=200)
            else:
                # if error send error to client
                str_error = ''
                for field, errors in form.errors.items():
                    str_error += field + ": "
                    for error in errors:
                        str_error += error + ', '
                return JsonResponse({"error": str_error[:-2]}, status=400)
        # request is not ajax
        else:
            return JsonResponse({"error": "Something went terribly wrong"}, status=400)

    def delete(self, request, id):
        """
        Delete Model train data record
        :param request:
        :param id: id to delete
        :return: None if delete, otherwise error
        """
        url_name = return_url_name(request.path)
        # check permission
        if not has_permission(request.user.role_id, url_name, request.method):
            return JsonResponse({"error": "No permission"}, status=403)
        if request.is_ajax:
            # get ModelTrainData record to delete
            delete_data = queries.get_model_train_data_by_id(id)
            # if delete data not found
            if not delete_data:
                return JsonResponse({"error": "Not found"}, status=404)
            # check if request user is owner
            if request.user != delete_data.added_by:
                return JsonResponse({"error": "No permission"}, status=403)
            # pass all: delete data
            delete_data.delete()
            # send to client
            return JsonResponse({}, status=200)
        else:
            # send error
            return JsonResponse({"error": "Something went terribly wrong"}, status=400)


class SearchModelTrainData(LoginRequiredMixin, View):
    login_url = '/login/'
    # add form
    form_class = forms.AddModelTrainData
    # search form
    search_form = forms.SearchModelTrainData

    def get(self, request):
        """
        Search for ModelTrainData
        :param request:
        :return: list of data by filter
        """
        filter = {}
        # get if user input
        data_name = request.GET.get("data")
        if data_name:
            filter['data'] = data_name
        model = request.GET.get("model")
        if model:
            filter['model'] = model
        added_by = request.GET.get("added_by")
        if added_by:
            filter['added_by'] = added_by
        result = request.GET.get("result")
        if result:
            filter['result__gte'] = result
        # get all data by filter
        data = queries.get_model_train_data_by_filter(**filter)
        # if exist, return to user
        if len(data) > 0:
            paginator = Paginator(data, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(
                request,
                'data_manager_app/modelTrainData.html',
                {
                    'form': self.form_class,
                    'datas': page_obj,
                    'search_form': self.search_form
                }
            )
        # else: return Not found
        else:
            return render(
                request,
                'data_manager_app/modelTrainData.html',
                {
                    'form': self.form_class,
                    'message': 'Not found',
                    'search_form': self.search_form
                }
            )


class Visualize(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        """
        :param request:
        :return: Visualize all models train on data records
        """
        data = queries.get_all_model_train_data().count()
        return render(
            request,
            'data_manager_app/modelTrainDataVisualize.html',
            {'number_of_records': data}
        )


class VisualizeModelTrainDataChart(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        """
        :param request:
        :return: API for visualize page above
        """
        # base color
        base_colors = [
            'red', 'orange', '#26E037', 'purple', 'blue', '2E251E',
            'IndianRed', 'Pink', 'LightSalmon', 'DarkKhaki', 'Fuchsia',
            'Lime', 'Aqua', 'MediumSlateBlue', 'Goldenrod', 'Maroon',
            'DimGray', 'Brown',
        ]
        # labels send to chart
        labels = [
            '< 30%',
            '30% - 50%',
            '50% - 80%',
            '80% - 90%',
            '>90%',
        ]
        # data send to chart
        data = []
        # color send to chart
        colors = []
        # data
        less_than_thirty = queries.get_model_train_data_by_filter(result__lte=30).count()
        data.append(less_than_thirty)
        thirty_to_fifty = queries.get_model_train_data_by_filter(result__gte=30, result__lte=50).count()
        data.append(thirty_to_fifty)
        fifty_to_eighty = queries.get_model_train_data_by_filter(result__gte=50, result__lte=80).count()
        data.append(fifty_to_eighty)
        eighty_to_ninety = queries.get_model_train_data_by_filter(result__gte=80, result__lte=90).count()
        data.append(eighty_to_ninety)
        more_than_ninety = queries.get_model_train_data_by_filter(result__gte=90).count()
        data.append(more_than_ninety)
        # append colors
        for i in range(len(data)):
            colors.append(base_colors[i])
        # send api to draw chart
        return JsonResponse(
            data={
                'labels': labels,
                'data': data,
                'color': colors,
            })
