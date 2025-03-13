from django.urls import path
from .views import *

urlpatterns = [
    path('wiki/articles', articles_list,name= 'articles_list'),
    path('wiki/article/<int:pk>',article_detail,name='articles_detail')
]

app_name = "wiki"