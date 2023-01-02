from django.urls import path, include
from rest_framework import routers
from .views import home_rest ,PostMVS, CategoryMVS

router = routers.DefaultRouter()
router.register("posts", PostMVS)
router.register("categories", CategoryMVS)
urlpatterns = [
    path('', home_rest),
    path("", include(router.urls))

]
