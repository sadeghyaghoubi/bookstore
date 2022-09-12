from django.contrib import admin
from .models import Book

# admin.site.register(Post)
@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author', 'price', 'date_time_create', 'date_time_modify',)
    ordering = ('date_time_create',)

