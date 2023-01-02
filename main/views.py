from django.shortcuts import HttpResponse

def home_page(request):
  return HttpResponse("This is the home page")