from rest_framework.pagination import PageNumberPagination

class CustomizedPagination(PageNumberPagination):
  page_size = 10