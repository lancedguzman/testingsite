from django.shortcuts import render
from .models import Article, ArticleCategory

def list_view(request):
    article_list = ArticleCategory.objects.all()
    return render(request, 'index.html', {"article_list": article_list})

def detail_view(request, category_id):
    article_category = ArticleCategory.objects.get(id=category_id)
    article_detail = Article.objects.filter(category=article_category)
    return render(request, 'article_content.html', {
      "article_category": article_category,
      "article_detail": article_detail,
      }
    )