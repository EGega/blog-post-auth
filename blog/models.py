from django.db import models

# Create your models here.

class Category(models.Model):
  category_name = models.CharField(max_length=50)

  def __str__(self):
    return self.category_name

class Post(models.Model):
  category_id = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
  title = models.CharField(max_length=50)
  content = models.TextField()
  status = models.BooleanField()
  created_date = models.DateTimeField()
  updated_date = models.DateTimeField()

  def __str__(self):
    return (f'Title: {self.title} - id: {self.id}')