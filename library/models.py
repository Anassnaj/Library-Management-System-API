from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=100, unique=True, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=255, null=True)
    membership_date = models.DateField(auto_now_add=True)
    membership_type = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=255, null=True)

class Book(models.Model):
    shelf_location = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=255, null=True)
    author = models.CharField(max_length=100, null=True)
    isbn = models.CharField(max_length=20, null=True)
    published_year = models.PositiveIntegerField(null=True)
    genre = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=20, null=True)
    total_copies = models.IntegerField(default=0)
    available_copies = models.IntegerField(default=0)

class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    checkout_date = models.DateField(null=True)
    due_date = models.DateField(null=True)
    return_date = models.DateField(null=True)
    status = models.CharField(max_length=20, null=True)
    fine_amount = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    renewals = models.IntegerField(null=True)
    notes = models.TextField(null=True)
