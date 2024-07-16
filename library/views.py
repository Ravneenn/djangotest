from django.http import HttpResponse
from django.shortcuts import render

from library.models import Article

# Create your views here.

def index(request):
    return render(request, 'libraries/index.html')
    

def reporters(request):
    return render(request, 'libraries/reporters.html')

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {"year": year, "article_list": a_list}
    return render(request, 'libraries/yearlist.html', context)

def month_archive(request, year , month):
    a_list = Article.objects.filter(pub_date__month=month)
    context = {"year": year, "month": month, "article_list": a_list}
    return render(request, 'libraries/monthlist.html',context)

def article_detail(request, pk):

    context = {"article": Article.objects.filter(pk = pk),}
    return render(request, 'libraries/articledetail.html', context)