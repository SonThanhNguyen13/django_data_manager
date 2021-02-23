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
from .views import views, dataset_manager_views, ai_model_manager_views, model_train_data_manager_view
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # views.py
    path("", views.Index.as_view(), name="home"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("change_password/", views.ChangePassword.as_view(), name="change_password"),
    # dataset_manager_views.py
        # category
    path("data/data_category/", dataset_manager_views.DataCategoryView.as_view(), name="data_category"),
    path("data/data_category/<int:pk>/", dataset_manager_views.EditDataCategory.as_view(), name="update_data_category"),
        # data
    path("data/", dataset_manager_views.DataPage.as_view(), name="data_page"),
    path("data/search", dataset_manager_views.SearchData.as_view(), name='search_data'),
    path("data/detail/<int:id>/", dataset_manager_views.DataDetail.as_view(), name="data_detail"),
    path('data/visualize/', dataset_manager_views.Visualize.as_view(), name='data_visualize'),
        # api for chart
    path('data/visualize/chart', dataset_manager_views.Chart.as_view(), name='data_chart'),
    path('data/visualize/chart_size', dataset_manager_views.ChartBySize.as_view(), name='data_chart_by_size'),
    path('data/visualize/chart_by_analyzed', dataset_manager_views.ChartByAnalyzed.as_view(), name='analyzed_data_chart'),
    # model_manager_views.py
    path("models/", ai_model_manager_views.AiModel.as_view(), name="ai_model"),
    path("models/<int:id>", ai_model_manager_views.AiModelDetail.as_view(), name='ai_model_detail'),
    path("models/search/", ai_model_manager_views.SearchAiModel.as_view(), name='search_ai_model'),
    path("model/visualize", ai_model_manager_views.ModelVisualize.as_view(), name='model_visualize'),
        # api for chart
    path('model/visualize/chart', ai_model_manager_views.ModelChart.as_view(), name='model_chart'),
    # model_train_data.py
    path("model_data/", model_train_data_manager_view.ModelTrainData.as_view(), name='model_train_data'),
    path("model_data/<int:id>", model_train_data_manager_view.ModelTrainDataDetail.as_view(), name='model_train_data_detail'),
    path('model_data/search/', model_train_data_manager_view.SearchModelTrainData.as_view(), name='model_train_data_search'),
        #   visualize
    path('model_data/visualize', model_train_data_manager_view.Visualize.as_view(), name='model_train_data_visualize'),
        # api for chart
    path('model_data/visualize/chart', model_train_data_manager_view.VisualizeModelTrainDataChart.as_view(), name='model_train_data_visualize_chart'),
    # for fun only
    path('fun/', views.Fun.as_view(), name='fun'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
