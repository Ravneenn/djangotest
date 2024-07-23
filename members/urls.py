from django.urls import path, include
from .  import views
from members.views import RegisterAPI, LoginAPI, UserAPI
from rest_framework import routers
from members.viewSets import *

router = routers.DefaultRouter()
router.register(r'workss', WorkViewSet)


urlpatterns = [
    path("", views.home , name="home" ),
    path('login_user', views.login_user, name='login_user'),
    path('profile/', views.profile, name='profile'),
    path('staffs/', views.staffs, name='staffs'),
    path('staffs/<str:staff>', views.staff, name='staffView'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
    path('api/', include(router.urls)),

    path('works', views.works, name='works'),
    path('work/<str:workName>', views.work, name='work'),
    path('update_work/<str:workName>', views.update_work, name='update_work'),
    path('create_work', views.createWork, name='create_work'),

    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('user/', UserAPI.as_view(), name='user'),

    path('403/', views.error_403_view, name='error_403'),
]
