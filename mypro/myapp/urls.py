from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [

  path('',views.add_todo,name="add_todo"),
  path('delete_g/<int:pk>',views.delete_g,name='delete'),
  path('edit_g/<int:pk>',views.edit_g,name='edit'),
]