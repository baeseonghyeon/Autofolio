from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('list' , views.draft_list , name="draft_list"),
	path('detail' , views.draft_detail , name="draft_detail"),
    path('create', views.draft, name='draft')
    
]
