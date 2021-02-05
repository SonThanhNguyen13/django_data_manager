import random
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash
from .check_permission import has_permission, return_url_name
from . import queries


class Index(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        datas = []
        categories = []
        all_category = queries.get_all_data_category()
        for i in all_category:
            data = queries.get_data_by_filter(num=5, reverse=True, data_category=i)
            if len(data) < 1:
                continue
            datas.append(data)
            categories.append(i)
        full_data = list(zip(categories, datas))
        return render(request, "data_manager_app/home.html", {'user': request.user, 'full_data': full_data})


class LoginView(View):
    def check_local_ip(self):
        pass

    def get(self, request):
        return render(request, 'data_manager_app/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password")
                return redirect("/login/")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("/login/")


class LogoutView(View):

    def get(self, request):
        logout(request)
        messages.error(request, "You have just logged out")
        return redirect("/login/")


class ChangePassword(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, "data_manager_app/changePassword.html")

    def post(self, request):
        url_name = return_url_name(request.path)
        if not has_permission(request.user.role_id, url_name, request.method):
            messages.error(request, "No permission")
            return redirect("/change_password/")
        password = request.POST.get('password')
        new_password = request.POST.get('new_password')
        cnf_password = request.POST.get('cnf_password')
        if new_password != cnf_password:
            messages.error(request, "Password does not match")
            return redirect("/change_password/")
        user = queries.get_user_by_username(request.user.username)
        # check password user send
        if not user.check_password(password):
            messages.error(request, "Invalid password")
            return redirect("/change_password/")
        # set new password
        user.set_password(new_password)
        user.save()
        # update session
        update_session_auth_hash(request, user)
        messages.info(request, "Change password successfully")
        return redirect("/change_password")


# fun
class Fun(View):
    def get(self, request):
        pages = [
            'home',
            'change_password',
            'data_category',
            'data_page',
            'data_visualize',
            'ai_model',
            'model_visualize',
            'model_train_data',
        ]
        page = random.choice(pages)
        return render(request, 'data_manager_app/fun.html', {'page':page})
