from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('request/', views.request_example, name='request'),
    path('request/app-attributes/', views.app_attributes_example, name='app_attributes'),
    path('request/middleware/', views.middleware_example, name='middleware'),
    path('request/querydict/', views.querydict_example, name='querydict'),
    path('response/', views.response_example, name='response'),
    path('response/subclasses/', views.response_subclasses_example, name='response_subclasses'),
    path('response/json/', views.json_response_example, name='json_response'),
    path('response/streaming/', views.stream_response_example, name='stream_response'),
    path('response/file/', views.file_response_example, name='file_response'),
    path('response/base/', views.response_base_example, name='response_base'),
    path('request/is-secure/', views.is_secure_example, name='is_secure'),
    path('home/', views.home_view, name='home_view'),
]
