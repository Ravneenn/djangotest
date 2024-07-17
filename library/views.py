from django.http import HttpResponse
from django.shortcuts import render

from library.models import Article

# Create your views here.



data = {
    "reporters":[
        {
            "full_name":"Muhammed Can Konulga"
        },
        {
            "full_name":"Tarık Ustaoğlu"
        },
        {
            "full_name":"Samet İsa Durmuş"
        },
        {
            "full_name":"Oktay Demir"
        },
        {
            "full_name":"Berat Ozan Kayabaşı"
        },
    ],
    "articles":[
        {
            "pub_date":"2024-07-17",
            "headline":"Makale Yazarı Oldum",
            "content":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "reporter":"Muhammed Can Konulga"
        },
        {
            "pub_date":"2024-07-15",
            "headline":"Makale Yazarı Olamamışım",
            "content":"It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).",
            "reporter":"Samet İsa Durmuş"
        },
        {
            "pub_date":"2024-04-25",
            "headline":"Makaleleler Müthiş",
            "content":"Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source.",
            "reporter":"Tarık Ustaoğlu"
        },
        {
            "pub_date":"2023-09-10",
            "headline":"Makale Yazarı Nasıl Olunur?",
            "content":"There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the",
            "reporter":"Oktay Demir"
        },
    ],

}

def index(request):
    context = {"reporters": data["reporters"], "articles": data["articles"]}
    return render(request, 'libraries/index.html', context)
    

def reporters(request):
    context = {"reporters": data["reporters"] }
    return render(request, 'libraries/reporters.html', context)

def articles(request):
    context = {"articles": data["articles"] }
    return render(request, 'libraries/articles.html', context)

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {"year": year, "article_list": a_list}
    return render(request, 'libraries/yearlist.html', context)

def month_archive(request, year , month):
    a_list = Article.objects.filter(pub_date__month=month)
    context = {"year": year, "month": month, "article_list": a_list}
    return render(request, 'libraries/monthlist.html',context)

def article_detail(request, pk):

    context = {"article": Article.objects.filter(pk = pk), "article_no": pk}
    return render(request, 'libraries/articledetail.html', context)