from django.contrib import admin
from django.urls import path, include
from . import views
app_name = "third_app"

urlpatterns = [
    path("", views.index, name="index")
]