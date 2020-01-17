from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):  
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name

class Publishing(models.Model):  
    name = models.TextField(default='')

    def __str__(self):
        return self.name

class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    publishing = models.ForeignKey(Publishing, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='books_prewies/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.title

class BooksRent(models.Model):
    rented_book = models.OneToOneField(
        Book, 
        on_delete=models.PROTECT,
        verbose_name="Арендованная книга",
        help_text="Книги нельзя сдать в аренду повторно"
        )
    book_renter = models.OneToOneField(
        User, 
        verbose_name="Арендатор", 
        on_delete=models.PROTECT, 
        blank=True,
        null=True,
        help_text="Пользователь может взять одну книгу")
    return_date = models.DateField(
        auto_now=False, 
        auto_now_add=False, 
        blank=True, 
        default=date.today,
        verbose_name="Дата возврата"
        )