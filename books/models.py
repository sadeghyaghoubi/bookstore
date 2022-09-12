from django.db import models
from django.urls import reverse


class Book (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2, )
    date_time_create = models.DateTimeField(auto_now_add=True)
    date_time_modify = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])
