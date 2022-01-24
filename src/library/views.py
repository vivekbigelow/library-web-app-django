from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse


from .models import Book, Author, Genre


# Create your views here.
def index(request):
  books = Book.objects.order_by('title')
  context = {
    'books':books,
  }

  return render(request, 'library/index.html', context)

def bookDetail(request, book_id):
  book = get_object_or_404(Book, pk=book_id)
  return render(request, 'library/book-detail.html', {'book': book})

def newBookForm(request):
  authors = Author.objects.all()
  genres = Genre.objects.all()

  return render(request, 'library/new-book-form.html', {'authors':authors, 'genres':genres})

def processNewBook(request):
  title = request.POST['title']
  author_id = request.POST['author']
  genre_id = request.POST['genre']

  if title and author_id and genre_id:
    author = get_object_or_404(Author, pk=author_id)
    genre = get_object_or_404(Genre, pk=genre_id)
    book = Book(title=title, author=author, genre=genre)
    book.save()
    return HttpResponseRedirect(reverse('library:index'))
  else:
    authors = Author.objects.all()
    genres = Genre.objects.all()
    return render(request, 'library/new-book-form.html', {'authors':authors, 'genres':genres, 'error_message': "Incorrect Book Data"})

  


