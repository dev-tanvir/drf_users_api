from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('viewsets-test', views.HelloViewsets, 'viewsets-test')
router.register('profile', views.UserProfileViewset)    #   here, no need for base-name as DRF 

urlpatterns = [
    path('apiview-test/', views.HelloAPIView.as_view(), name='Apiview Test'),
    path('', include(router.urls))
]

