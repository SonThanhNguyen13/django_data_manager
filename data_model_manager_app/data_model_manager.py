import random
from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from . import forms
from . import queries
from django.views import View
from .check_permission import has_permission, return_url_name


class Model_train_data(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        data = queries.get_model_train_data(reverse=True)
        return HttpResponse(data)