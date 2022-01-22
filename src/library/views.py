from django.http import HttpResponse
from django.template import loader

from .models import Book

# Create your views here.
def index(request):
  books = Book.objects.order_by('title')
  template = loader.get_template('library/index.html')
  context = {
    'books':books,
  }

  return HttpResponse(template.render(context, request))

def bookDetail(request, book_id):
  response = "You're looking at the details of book %s."
  return HttpResponse(response % book_id)

