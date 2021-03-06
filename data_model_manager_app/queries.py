from . import models
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count, Sum


# permission
def get_permission_by_role(role):
    # get all permissions a role has
    permissions = models.RoleHasPermission.objects.filter(role=role)
    # convert to id
    permissions = [i.permission.permission_id for i in permissions]
    return permissions


def get_permissions_by_page_name(url_name, method):
    try:
        check_permission = models.Permission.objects.get(method=method, permission_url_name=url_name).permission_id
        return check_permission
    except ObjectDoesNotExist:
        return None


# user
def get_user_by_username(username):
    try:
        user = models.User.objects.get(username=username)
        return user
    except ObjectDoesNotExist:
        return None


def get_all_user():
    try:
        users = models.User.objects.all()
        return users
    except ObjectDoesNotExist:
        return None


def get_all_user_by_role(role_name):
    try:
        role = get_role_by_name(role_name)
        users = models.User.objects.filter(role=role)
        return users
    except ObjectDoesNotExist:
        return None


# role
def get_role_by_name(role_name):
    try:
        role = models.Role.objects.get(role_name=role_name)
        return role
    except ObjectDoesNotExist:
        return None


# data
def get_all_data(reverse=False):
    all_data = models.Dataset.objects.all()
    if reverse:
        return all_data.order_by("-data_id")
    return all_data


def get_data_by_id(id):
    try:
        data = models.Dataset.objects.get(data_id=id)
        return data
    except ObjectDoesNotExist:
        return None


def get_data_by_analyzed():
    try:
        data = models.Dataset.objects.values('analyzed').annotate(dcount=Count('analyzed'))
        return data
    except ObjectDoesNotExist:
        return None


def get_data_by_filter(reverse=False, num=None, **kwargs):
    try:
        data = models.Dataset.objects.filter(**kwargs)
        if reverse:
            data = data.order_by('-data_id')
        if num:
            data = data[:num]
        return data
    except ObjectDoesNotExist:
        return None


def get_sum_data_size():
    try:
        data = models.Dataset.objects.all().aggregate(Sum('size_on_disk'))
        return data
    except ObjectDoesNotExist:
        return None


def get_sum_data_size_by_category(category):
    try:
        category = models.DataCategory.objects.get(name=category)
        data = models.Dataset.objects.filter(data_category=category).aggregate(Sum('size_on_disk'))
        return data
    except ObjectDoesNotExist:
        return None


# data category
def get_all_data_category(reverse=False):
    all_data_category = models.DataCategory.objects.all()
    if reverse:
        return all_data_category.order_by("-data_category_id")
    return all_data_category


def get_data_category_by_filter(**kwargs):
    try:
        data_category = models.DataCategory.objects.get(**kwargs)
        return data_category
    except ObjectDoesNotExist:
        return None


# models
def get_all_ai_model(reverse=False):
    all_ai_model = models.AiModel.objects.all()
    if reverse:
        return all_ai_model.order_by("-model_id")
    else:
        return all_ai_model


def get_ai_model_by_id(id):
    try:
        model = models.AiModel.objects.get(model_id=id)
        return model
    except ObjectDoesNotExist:
        return None


def get_model_by_filter(reverse=False, **kwargs):
    try:
        data = models.AiModel.objects.filter(**kwargs)
        if reverse:
            return data.order_by('-model_id')
        return data
    except ObjectDoesNotExist:
        return None


# Model train data:
def get_all_model_train_data(reverse=False):
    try:
        data = models.ModelTrainData.objects.all()
        if reverse:
            data = data.order_by('-id')
        return data
    except ObjectDoesNotExist:
        return None


def get_model_train_data_by_id(id):
    try:
        data = models.ModelTrainData.objects.get(id=id)
        return data
    except ObjectDoesNotExist:
        return None


def get_model_train_data_by_filter(**kwargs):
    try:
        data = models.ModelTrainData.objects.filter(**kwargs).order_by('-id')
        return data
    except ObjectDoesNotExist:
        return None
