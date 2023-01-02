from rest_framework import serializers
from .models import Category, Post

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id', 'category_name']

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ['id', 'category_id', 'title', 'content', 'status', 'created_date', 'updated_date']