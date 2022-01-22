from django.shortcuts import render, get_object_or_404


from .models import Book

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

