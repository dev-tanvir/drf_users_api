from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('viewsets-test', views.HelloViewsets, 'viewsets-test')
router.register('profile', views.UserProfileViewset)    #   here, no need for base-name as 'UserProfileViewset' is a ModelViewSet
router.register('login', views.LoginViewSet, base_name='login')     # we are using basename as
                                                                    # 'LoginViewSet' is ModelViewSet

urlpatterns = [
    path('apiview-test/', views.HelloAPIView.as_view(), name='Apiview Test'),
    path('', include(router.urls))
]

