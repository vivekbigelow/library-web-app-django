from django.urls import path

from . import views

app_name = 'library'
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:book_id>/', views.bookDetail, name='bookDetail'),
  path('new-book-form/', views.newBookForm, name='newBookForm'),
  path('process-new-book', views.processNewBook, name='processNewBook')
]