from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin  # new
from django.views.generic import ListView, DetailView # new
from .models import Book

class BookListView(LoginRequiredMixin,ListView):
	model = Book
	context_object_name = "book_list" # new
	template_name = "books/book_list.html"
	
class BookDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView): # new
	model = Book
	context_object_name = "book"
	template_name = "books/book_detail.html"
	permission_required = "books.special_status" # new


