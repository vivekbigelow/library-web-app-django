from turtle import title
from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
  firstName = models.CharField(max_length=250, blank=True)
  lastName = models.CharField(max_length=250, blank=True)

  def __str__(self):
    self.firstName + self.lastName
    return self.firstName + ' ' + self.lastName

class Genre(models.Model):
  name = models.CharField(max_length=250, blank=True)

  def __str__(self):
    return self.name

class Book(models.Model):
  title = models.CharField(max_length=250)
  author = models.ForeignKey(Author, on_delete=models.RESTRICT)
  genre = models.ForeignKey(Genre, on_delete=models.RESTRICT)

  def __str__(self):
    return self.title

