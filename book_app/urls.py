from django.urls import path
from . import views
from .views import PublisherDetail

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
    path('authors/', views.AuthorList.as_view(), name='author-list'),
    path('authors/<int:pk>/', views.AuthorDetail.as_view(), name='author-detail'),
    path('publishers/', views.PublisherList.as_view(), name='publisher-list'),
    path('publishers/<int:pk>/', PublisherDetail.as_view(), name='publisher-detail'),
]