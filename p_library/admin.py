from django.contrib import admin
from p_library.models import Book, Author, Publishing, BooksRent

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Publishing)
class PublishingAdmin(admin.ModelAdmin):
    pass

@admin.register(BooksRent)
class BooksRentAdmin(admin.ModelAdmin):
    list_display = ('rented_book', 'book_renter',)