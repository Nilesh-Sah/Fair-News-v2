from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home , name='home'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('create/', views.create_article , name='create_article'),
    
]