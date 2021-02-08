import random
from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from data_model_manager_app import forms
from data_model_manager_app import queries
from django.views import View
from data_model_manager_app.check_permission import has_permission, return_url_name


class AiModel(LoginRequiredMixin, View):
    login_url = "/login/"
    form_class = forms.AiModelForm
    search_form = forms.SearchAiModelForm

    def get(self, request):
        # get all ai_model from database
        models = queries.get_all_ai_model(reverse=True)
        # paginator
        paginator = Paginator(models, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # add form
        form = self.form_class
        # render
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
        # get url_name to check permission
        url_name = return_url_name(request.path)
        # check permission
        if not has_permission(request.user.role_id, url_name, request.method):
            return JsonResponse({'error': 'No permission'}, status=403)
        # check if request is ajax
        elif request.is_ajax():
            form = self.form_class(request.POST)
            # check if form is valid
            if form.is_valid():
                instance = form.save(commit=False)
                # model_owner = add user
                instance.model_owner = request.user
                instance.save()
                # send to client
                return JsonResponse({'Added model': instance.model_name}, status=200)
            else:
                # Make error string
                str_error = ''
                for field, errors in form.errors.items():
                    # add error field
                    str_error += field + ": "
                    # add all error in field
                    for error in errors:
                        str_error += error + ', '
                return JsonResponse({"error": str_error[:-2]}, status=400)
        # request not ajax
        else:
            return JsonResponse({"Error": "Something when terribly wrong"}, status=400)


class AiModelDetail(LoginRequiredMixin, View):
    login_url = '/login/'
    form_class = forms.AiModelForm

    def post(self, request, id):
        # get url_name
        url_name = return_url_name(request.path)
        # check permission
        if not has_permission(request.user.role_id, url_name, request.method):
            return JsonResponse({'error': 'No permission'}, status=403)
        # check if request is ajax
        if request.is_ajax():
            # get update model
            update_model = queries.get_ai_model_by_id(id)
            # check if model exist
            if update_model:
                # check if user request is the owner
                if update_model.model_owner == request.user:
                    form = self.form_class(request.POST, instance=update_model)
                    # check if form is valid
                    if form.is_valid():
                        instance = form.save()
                        return JsonResponse({'Edit model': instance.model_name}, status=200)
                    else:
                        # make error string
                        str_error = ''
                        for field, errors in form.errors.items():
                            # add all error fields
                            str_error += field + ": "
                            # add all error of one field
                            for error in errors:
                                str_error += error + ', '
                        return JsonResponse({"error": str_error[:-2]}, status=400)
                else:
                    # user is not the owner
                    return JsonResponse({'error': 'No permission'}, status=403)
                # if update data not found
            else:
                return HttpResponse("404 Not found")
        # request not ajax
        else:
            return JsonResponse({'error': 'Something when terribly wrong'})

    def delete(self, request, id):
        url_name = return_url_name(request.path)
        # check permission before delete
        if not has_permission(request.user.role_id, url_name, request.method):
            return JsonResponse({'error': 'No permission'}, status=403)
        # check if request is ajax
        if request.is_ajax():
            # get delete model
            delete_model = queries.get_ai_model_by_id(id)
            # check if model exist
            if delete_model:
                # check user request == owner
                if delete_model.model_owner == request.user:
                    delete_model.delete()
                    return JsonResponse({}, status=200)
                # no permission if not owner
                else:
                    return JsonResponse({'error': 'No permission'}, status=403)
            # delete model not found
            else:
                return HttpResponse("404 Not found")
        # request not ajax
        else:
            return JsonResponse({'error': 'Something when terribly wrong'})


class ModelVisualize(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        # get count number
        number_of_models = queries.get_all_ai_model().count()
        # get count user by role 'user'
        number_of_users = queries.get_all_user_by_role('user').count()
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
    # add, edit form
    form_class = forms.AiModelForm
    # search form
    search_form = forms.SearchAiModelForm

    def get(self, request):
        # search query
        query = {}
        # get data submit by user
        model_name = request.GET.get('model_name')
        model_owner = request.GET.get('model_owner')
        # if user submit model_name
        if model_name:
            query['model_name'] = model_name
        # if user submit model owner
        if model_owner:
            query['model_owner'] = model_owner
        # if nothing was submit, redirect to model page
        if len(query) < 1:
            return redirect('/models/')
        # get models by query
        search_models = queries.get_model_by_filter(True, **query)
        # if there is something match, return search data
        if len(search_models) > 0:
            # paginator
            paginator = Paginator(search_models, 10)
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
        # return not found if no data
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
        # base color
        base_colors = [
            'red', 'blue', 'orange', 'purple', '#2E251E', '#26E037',
            'IndianRed', 'Pink', 'LightSalmon', 'DarkKhaki', 'Fuchsia',
            'Lime', 'Aqua', 'MediumSlateBlue', 'Goldenrod', 'Maroon',
            'DimGray', 'Brown',
        ]
        # labels send to chart
        labels = []
        # data send to chart
        models = []
        # color send to chart
        colors = []
        # get user list with role = 'user'
        all_users = queries.get_all_user_by_role('user')
        for i in range(len(all_users)):
            # count all models user own
            number_of_models = queries.get_model_by_filter(model_owner=all_users[i]).count()
            # if user own any model
            if number_of_models > 0:
                labels.append(all_users[i].username)
                models.append(number_of_models)
                # append colors from base colors. If base color is full, append from beginning
            colors.append(base_colors[i % len(base_colors)])
        # check if last color == first color
        if len(colors) > 1:
            if colors[-1] == colors[0]:
                # copy base color
                new_colors = base_colors.copy()
                # remove 2 last color
                new_colors.remove(colors[-1])
                new_colors.remove(colors[-2])
                # random color in list
                colors[-1] = random.choice(new_colors)
        # send api to draw chart
        return JsonResponse(
            data={
                'labels': labels,
                'data': models,
                'color': colors,
            })
