from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    date_published = models.DateField(auto_now_add=True)
    number_of_pages = models.IntegerField(default=1)
    number_of_chapters = models.IntegerField(default=1)
    book_cover = models.ImageField(upload_to='book_covers', default='book_covers/default_book.png')
    
    def __str__(self):
        return self.name
