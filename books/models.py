from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Book (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2, )
    date_time_create = models.DateTimeField(auto_now_add=True)
    date_time_modify = models.DateTimeField(auto_now=True)
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])


class Comment (models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, )
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments', )
    text = models.TextField()
    date_time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

