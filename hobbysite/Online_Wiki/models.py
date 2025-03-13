from django.db import models
from django.urls import reverse

# Create your models here.

class Article_Category(models.Model):
    name = models.CharField(max_length=255)
    description_field = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['created_on']
        verbose_name = 'Article Category'
        verbose_name_plural = 'Article Categories'

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    article_category = models.ForeignKey(Article_Category,on_delete=models.CASCADE)
    entry_field = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article_detail', args=[self.pk])
