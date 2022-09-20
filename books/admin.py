from django.contrib import admin
from .models import Book, Comment
# admin.site.register(Post)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_time_create', 'date_time_modify',)
    ordering = ('date_time_create',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'text', 'date_time_create', 'is_active', 'recommend' )
    ordering = ('date_time_create',)

