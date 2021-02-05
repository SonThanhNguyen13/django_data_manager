from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View
from .check_permission import has_permission, return_url_name
from . import forms
from . import queries


class ModelTrainData(LoginRequiredMixin, View):
    login_url = '/login/'
    form_class = forms.AddModelTrainData
    search_form = forms.SearchModelTrainData

    def get(self, request):
        data = queries.get_model_train_data(reverse=True)
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

    def post(self, request):
        url_name = return_url_name(request.path)
        if not has_permission(request.user.role_id, url_name, request.method):
            return JsonResponse({'error': 'No permission'}, status=403)
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.added_by = request.user
                instance.save()
                return JsonResponse({'Added data': "Hello"}, status=200)
            else:
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
        """Update data"""
        url_name = return_url_name(request.path)
        if not has_permission(request.user.role_id, url_name, request.method):
            return JsonResponse({"error": "No permission"}, status=403)
        if request.is_ajax:
            update_data = queries.get_model_train_data_by_id(id)
            if not update_data:
                return HttpResponse('404 not found')
            if request.user != update_data.added_by:
                return JsonResponse({"error": "No permission"}, status=403)
            form = self.form_class(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.added_by = request.user
                instance.save()
                # send to client side.
                return JsonResponse({"Edit data": {"instance": "Success"}}, status=200)
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
            return JsonResponse({"error": "No permission"}, status=403)
        elif request.is_ajax:
            delete_data = queries.get_model_train_data_by_id(id)
            if request.user != delete_data.added_by:
                return JsonResponse({"error": "No permission"}, status=403)
            # fix sau khi co du model
            if not delete_data:
                return JsonResponse({"error": "Not found"}, status=404)
            delete_data.delete()
            return JsonResponse({}, status=200)
        else:
            return JsonResponse({"error": "Something went terribly wrong"}, status=400)


class SearchModelTrainData(LoginRequiredMixin, View):
    login_url = '/login/'
    form_class = forms.AddModelTrainData
    search_form = forms.SearchModelTrainData

    def get(self, request):
        filter = {}
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
            filter['result'] = result
        data = queries.get_model_train_data_by_filter(**filter)
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