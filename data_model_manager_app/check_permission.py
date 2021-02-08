from data_model_manager_app import queries
from django.urls import resolve


def return_url_name(url):
    return resolve(url).url_name


def has_permission(role, url_name, method):
    user_permissions = queries.get_permission_by_role(role)
    action_permission = queries.get_permissions_by_page_name(url_name, method)
    if action_permission in user_permissions:
        return True
    return False


def check_local_ip(request):
    ip = get_client_ip(request)
    # if ip khong thuoc bang ip:
    #     request.user.role = queries.get_role_by_name('guest')
    return request


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
