from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Book
from django.urls import reverse_lazy

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'books'   #be dard halghe for too safhe listemoon mikhore
    template_name = 'book/book_list.html'
    paginate_by = 4


# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = 'book/book_detail.html'

def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book_comments = book.comments.all()
    return render(request, 'book/book_detail.html', {'book': book, 'comments': book_comments})



class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'book/book_create.html'
    fields = ['title', 'description', 'author', 'price', 'cover', ]


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'description', 'author', 'price', 'cover', ]
    template_name = 'book/book_update.html'


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'book/book_delete.html'
    success_url = reverse_lazy('book_list')



