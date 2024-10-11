
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogHome, name='blogHome'),
    path('myform/', views.my_form_view, name='my_form'),
    path('blogpost/',views.blogPost,name="blogPost"),
    path('add/',views.add,name="add"),

]