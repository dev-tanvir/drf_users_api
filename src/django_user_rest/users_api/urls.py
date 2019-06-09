from django.urls import path
from . import views

urlpatterns = [
    path('apiview-test/', views.HelloAPIView.as_view(), name='Apiview Test'),
]