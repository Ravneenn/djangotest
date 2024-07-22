from django.urls import path
from .  import views
from members.views import RegisterAPI, LoginAPI, UserAPI

urlpatterns = [
    path("", views.home , name="home" ),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
    path('works', views.works, name='works'),
    path('work/<str:workName>', views.work, name='work'),
    path('create_work', views.createWork, name='create_work'),

    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('user/', UserAPI.as_view(), name='user'),

    path('403/', views.error_403_view, name='error_403'),
]
