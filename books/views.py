from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin  # new
from django.views.generic import ListView, DetailView # new
from .models import Book
from django.db.models import Q # new

class BookListView(LoginRequiredMixin,ListView):
	model = Book
	context_object_name = "book_list" # new
	template_name = "books/book_list.html"
	
class BookDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView): # new
	model = Book
	context_object_name = "book"
	template_name = "books/book_detail.html"
	permission_required = "books.special_status" # new

class SearchResultsListView(ListView): # new
	model = Book
	context_object_name = "book_list"
	template_name = "books/search_results.html"
	#queryset = Book.objects.filter(title__icontains="beginners") # new
	queryset = Book.objects.all().prefetch_related('reviews__author',) # new
	
	def get_queryset(self): # new
		query = self.request.GET.get("q")
		return Book.objects.filter(
		Q(title__icontains=query) | Q(title__icontains=query)
		)

