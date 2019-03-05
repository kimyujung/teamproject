from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>/', views.detail, name = "detail"),
    path('new/', views.new, name = "new"),
    path('newblog/', views.blogpost, name = "newblog"),
    path('<int:blog_id>/edit', views.edit, name="edit"),
    path('<int:blog_id>/delete', views.delete, name="delete"),
    path('<int:blog_id>/comment/create/', views.comment_create, name="comment_create"),
    path('<int:blog_id>/comment/delete/', views.comment_delete, name="comment_delete"),
]