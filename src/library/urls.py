from django.urls import path

from . import views

app_name = 'library'
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:pk>/', views.BookDetailView.as_view(), name='bookDetail'),
  path('author/<int:author_id>/', views.authorDetail, name='authorDetail'),
  path('genre/<int:genre_id>', views.genreDetail,name='genreDetail'),
  path('new-book-form/', views.newBookForm, name='newBookForm'),
  path('process-new-book', views.processNewBook, name='processNewBook'),
]