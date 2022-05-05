
from pydoc import describe
from django.db import models

class Emp(models.Model):
    name = models.CharField(max_length=255,verbose_name="name")
    age = models.IntegerField(verbose_name="age")
    salary = models.DecimalField(decimal_places=10,max_digits=100000000000,verbose_name="salary")
    email =models.EmailField(blank = True)
    number=models.IntegerField(verbose_name="number")
    country=models.CharField(max_length=255,verbose_name="country")



class Category(models.Model):
    category_description = models.CharField(max_length=5000)

    def __str__(self):
        return self.category_description

class Book(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.IntegerField(null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.category_id

class Author(models.Model):
    author_name = models.CharField(max_length=200)

class Author_Book(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

class Book_Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True)
    order_date = models.DateField()

class Ordering(models.Model):
    order = models.ForeignKey('Book_Order', on_delete=models.CASCADE, null=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    price = models.IntegerField(null=True)



