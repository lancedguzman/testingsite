from django.db import models
from django.urls import reverse

# should be sorted by name in ascending order
class ArticleCategory(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()

  class Meta:
    ordering = ["name"]
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("blog:detail_view", args=[str(self.id)])

#should be sorted by data it was created in descending order
class Article(models.Model):
  title = models.CharField(max_length=255)
  category = models.ForeignKey(
    ArticleCategory,
    on_delete=models.SET_NULL,
    null=True
  )
  entry = models.TextField()
  created_on = models.DateTimeField(auto_now_add = True)
  updated_on = models.DateTimeField(auto_now = True)

  class Meta:
    ordering = ["-created_on"]
  
  def __str__(self):
    return self.title