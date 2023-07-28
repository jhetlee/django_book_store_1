from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Book
from django.db.models import Avg

# Create your views here.

def index(request):
    books = Book.objects.all().order_by("-title") # order by use to sort in databse level ascending order, order_by("-title") descending
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html", {
        "books":books,
        "total_number_of_books":num_books,
        "average_rating":avg_rating,

    })

def book_detail(request, slug):
    """try:
        books = Book.objects.get(pk=id)
    except:
        raise Http404()
    """
    books = get_object_or_404(Book, slug=slug) ## alternate from try excep
    return render(request, "book_outlet/book_detail.html", {
        "title": books.title,
        "author": books.author,
        "rating": books.rating,
        "is_bestselling": books.is_bestselling
    })