from django.urls import path


from . import views


urlpatterns = [
    path("", views.index , name="home" ),
    path("index/", views.index ),
    path("reporters/", views.reporters, name="reporters" ),
    path("articles/", views.articles, name="articles" ),
    path("articles/<int:year>/", views.year_archive, name="archive_year"),
    path("articles/<int:year>/<int:month>/", views.month_archive, name="archive_month"),
    path("article/<int:pk>/", views.article_detail, name="article_detail"),
    path("reporter/<int:pk>/", views.reporter_detail, name="reporter_detail"),
]