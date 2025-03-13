from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.

def articles_list(request):
    articles = Article.objects.all()

    return render(request, 'articles.html', {'Articles_List':articles})

def article_detail(request,pk):
    article = get_object_or_404(Article, pk=pk)

    return render(request,'article_detail.html',{'Article_Detail': article})