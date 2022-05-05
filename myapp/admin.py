from django.contrib import admin
from .models import Emp, Book_Order, Category, Book, Author, Author_Book, Customer, Ordering
# Register your models here.
admin.site.register(Emp)
admin.site.register(Book_Order)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Author_Book)
admin.site.register(Customer)
admin.site.register(Ordering)