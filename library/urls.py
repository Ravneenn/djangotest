from django.urls import path


from . import views


urlpatterns = [
    path("", views.index ),
    path("index/", views.index ),
    path("reporters/", views.reporters ),
    path("articles/<int:year>/", views.year_archive),
    path("articles/<int:year>/<int:month>/", views.month_archive),
    path("article/<int:pk>/", views.article_detail),
]