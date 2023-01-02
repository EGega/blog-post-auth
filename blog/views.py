from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import action,  api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from .pagination import CustomizedPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, BasePermission, SAFE_METHODS

from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.

@api_view(['GET'])
def home_rest(request):
  return Response({'message': "This is the home page"})




class PostMVS(ModelViewSet):
  
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  pagination_class = CustomizedPagination
  filter_backends = [SearchFilter, OrderingFilter]
  permission_classes = [IsAuthenticatedOrReadOnly]
  search_fields = ['title', 'content', 'status', ]



class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class CategoryMVS(ModelViewSet):
  
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  pagination_class = CustomizedPagination
  filter_backends = [SearchFilter, OrderingFilter]
  search_fields = ['category_name', 'id']
  permission_classes = [IsAdminUser | ReadOnly]
