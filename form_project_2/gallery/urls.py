from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('load_file',views.GalleryView.as_view()),
    path('list_file',views.ListGallery.as_view()),
]