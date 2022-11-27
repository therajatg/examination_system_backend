from django.contrib import admin
from django.urls import path,include
from .views import CourseViewSet
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'courses', CourseViewSet)
urlpatterns = [    
    path('',include(router.urls))
]