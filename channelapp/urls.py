# urls.py
from django.urls import path
from .views import template_view

urlpatterns = [
    path('template_view/', template_view)
]
