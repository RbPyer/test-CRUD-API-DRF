from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('api/v1/microservice/', MicroserviceAPIList.as_view()),
    path('api/v1/microservice/<int:pk>/', MicroserviceAPIUpdate.as_view()),
    path('api/v1/microservice/<int:pk>/', MicroserviceAPIDestroy.as_view()),
    path('api/v1/drf-auth/login/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
