from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic


from .models import Book, Author, Genre


# Create your views here.
def index(request):
  books = Book.objects.order_by('title')
  context = {
    'books':books,
  }

  return render(request, 'library/index.html', context)

class BookDetailView(generic.DetailView):
  model = Book
  template_name = 'library/book-detail.html'

def authorDetail(request, author_id):
  author = get_object_or_404(Author, pk=author_id)
  books = Book.objects.filter(author_id=author_id)
  return render(request, 'library/author-detail.html', {"author":author, "books":books})

def genreDetail(request, genre_id):
  genre = get_object_or_404(Genre, pk=genre_id)
  books = Book.objects.filter(genre_id=genre_id)
  return render(request, 'library/genre-detail.html', {"genre":genre, "books":books})

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
    return HttpResponseRedirect(reverse('library:bookDetail', args=(book.pk,)))
  else:
    authors = Author.objects.all()
    genres = Genre.objects.all()
    return render(request, 'library/new-book-form.html', {'authors':authors, 'genres':genres, 'error_message': "Improper Book Data"})  

  


