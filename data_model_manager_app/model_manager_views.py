import random
from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from . import forms
from . import queries
from django.views import View
from .check_permission import has_permission, return_url_name


class AiModel(LoginRequiredMixin, View):
    login_url = "/login/"
    form_class = forms.AiModelForm
    search_form = forms.SearchAiModelForm

    def get(self, request):
        models = queries.get_all_ai_model(reverse=True)
        paginator = Paginator(models, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        form = self.form_class
        return render(
            request,
            'data_manager_app/aiModel.html',
            {
                'form': form,
                'models': page_obj,
                'search_form': self.search_form
            }
        )

    def post(self, request):
        url_name = return_url_name(request.path)
        if not has_permission(request.user.role_id, url_name, request.method):
            return JsonResponse({'error': 'No permission'}, status=400)
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.model_owner = request.user
                instance.save()
                return JsonResponse({'Added model': instance.model_name}, status=200)
            else:
                str_error = ''
                for field, errors in form.errors.items():
                    str_error += field + ": "
                    for error in errors:
                        str_error += error + ', '
                return JsonResponse({"error": str_error[:-2]}, status=400)
        else:
            return JsonResponse({"Error": "Something when terribly wrong"}, status=400)


class AiModelDetail(LoginRequiredMixin, View):
    login_url = '/login/'
    form_class = forms.AiModelForm

    def post(self, request, id):
        url_name = return_url_name(request.path)
        if not has_permission(request.user.role_id, url_name, request.method):
            return JsonResponse({'error': 'No permission'}, status=400)
        if request.is_ajax():
            update_model = queries.get_ai_model_by_id(id)
            if update_model.model_owner == request.user:
                if update_model:
                    form = self.form_class(request.POST, instance=update_model)
                    if form.is_valid():
                        instance = form.save()
                        return JsonResponse({'Edit model': instance.model_name}, status=200)
                    else:
                        str_error = ''
                        for field, errors in form.errors.items():
                            str_error += field + ": "
                            for error in errors:
                                str_error += error + ', '
                        return JsonResponse({"error": str_error[:-2]}, status=400)
                else:
                    return HttpResponse("404 Not found")
            else:
                return JsonResponse({'error': 'No permission'}, status=400)
        else:
            return JsonResponse({'error': 'Something when terribly wrong'})

    def delete(self, request, id):
        url_name = return_url_name(request.path)
        if not has_permission(request.user.role_id, url_name, request.method):
            return JsonResponse({'error': 'No permission'}, status=400)
        if request.is_ajax():
            delete_model = queries.get_ai_model_by_id(id)
            if delete_model.model_owner == request.user:
                if delete_model:
                    delete_model.delete()
                    return JsonResponse({}, status=200)
                else:
                    return HttpResponse("404 Not found")
            else:
                return JsonResponse({'error': 'No permission'}, status=400)
        else:
            return JsonResponse({'error': 'Something when terribly wrong'})


class ModelVisualize(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        number_of_models = queries.get_all_ai_model().count()
        number_of_users = queries.get_all_user().count()
        return render(
            request,
            'data_manager_app/modelVisualize.html',
            {
                'number_of_users': number_of_users,
                'number_of_models': number_of_models,
            }
        )


class SearchAiModel(LoginRequiredMixin, View):
    login_url = '/login/'
    form_class = forms.AiModelForm
    search_form = forms.SearchAiModelForm

    def get(self, request):
        query = {}
        model_name = request.GET.get('model_name')
        model_owner = request.GET.get('model_owner')
        if model_name:
            query['model_name'] = model_name
        if model_owner:
            query['model_owner'] = model_owner
        if len(query) < 1:
            return redirect('/models/')
        models = queries.get_model_by_filter(True, **query)
        if len(models) > 0:
            paginator = Paginator(models, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(
                request,
                'data_manager_app/aiModel.html',
                {
                    'form': self.form_class,
                    'models': page_obj,
                    'search_form': self.search_form
                }
            )
        else:
            return render(
                request,
                'data_manager_app/aiModel.html',
                {
                    'form': self.form_class,
                    'message': 'Not found',
                    'search_form': self.search_form
                }
            )


class ModelChart(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        base_colors = [
            'red', 'blue', 'orange', 'purple', '#2E251E', '#26E037',
            'IndianRed', 'Pink', 'LightSalmon', 'DarkKhaki', 'Fuchsia',
            'Lime', 'Aqua', 'MediumSlateBlue', 'Goldenrod', 'Maroon',
            'DimGray', 'Brown',
        ]
        labels = []
        models = []
        colors = []
        all_users = queries.get_all_user()
        for i in range(len(all_users)):
            labels.append(all_users[i].username)
            models.append(queries.get_model_by_filter(model_owner=all_users[i]).count())
            # append colors from base colors. If base color is full, append from beginning
            colors.append(base_colors[i % len(base_colors)])
        # check if last color == first color
        print(labels, models)
        if len(colors) > 1:
            if colors[-1] == colors[0]:
                new_colors = base_colors.copy()
                new_colors.remove(colors[-1])
                new_colors.remove(colors[-2])
                colors[-1] = random.choice(new_colors)
        return JsonResponse(
            data={
                'labels': labels,
                'data': models,
                'color': colors,
            })
