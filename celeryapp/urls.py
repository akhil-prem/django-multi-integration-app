# urls.py
from django.urls import path
from .views import add_view

urlpatterns = [
    path('add_view/', add_view)
]
