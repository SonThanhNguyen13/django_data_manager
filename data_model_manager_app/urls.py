"""django_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views, data_manager_views, model_manager_views, data_model_manager
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.Index.as_view(), name="home"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("change_password/", views.ChangePassword.as_view(), name="change_password"),
    path("data/data_category/", data_manager_views.DataCategoryView.as_view(), name="data_category"),
    path("data/data_category/<int:pk>/", data_manager_views.EditDataCategory.as_view(), name="update_data_category"),
    path("data/", data_manager_views.DataPage.as_view(), name="data_page"),
    path("data/search", data_manager_views.SearchData.as_view(), name='search_data'),
    path("data/detail/<int:id>/", data_manager_views.DataDetail.as_view(), name="data_detail"),
    path('data/visualize/', data_manager_views.Visualize.as_view(), name='data_visualize'),
    path('data/visualize/chart', data_manager_views.Chart.as_view(), name='data_chart'),
    path('data/visualize/chart_by_analyzed', data_manager_views.ChartByAnalyzed.as_view(), name='analyzed_data_chart'),
    path("models/", model_manager_views.AiModel.as_view(), name="ai_model"),
    path("models/<int:id>", model_manager_views.AiModelDetail.as_view(), name='ai_model_detail'),
    path("models/search/", model_manager_views.SearchAiModel.as_view(), name='search_ai_model'),
    path("model/visualize", model_manager_views.ModelVisualize.as_view(), name='model_visualize'),
    path('model/visualize/chart', model_manager_views.ModelChart.as_view(), name='model_chart'),
    path("model_data/", data_model_manager.Model_train_data.as_view(), name='model_and_data'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)