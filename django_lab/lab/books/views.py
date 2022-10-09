from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.utils import timezone

from .forms import BooksForm
from .models import Book


# Create your views here.
@login_required(login_url="/login/")
def index(request: HttpRequest) -> HttpResponse:
    books = Book.objects.order_by("-create_time")
    context = {"books": books}

    return render(request, "books/index.html", context)


@login_required(login_url="/login/")
def add(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        book = BooksForm(request.POST)
        if book.is_valid():
            book = book.save(commit=False)

            book.create_time = timezone.now()
            book.last_edit_time = timezone.now()
            book.save()
            return redirect("view_books")
        else:
            context = {"form": book}
            return render(request, "books/add.html", context)
    else:
        book = BooksForm()
        context = {"form": book}
        return render(request, "books/add.html", context)


@login_required(login_url="/login/")
def get(request: HttpRequest, id: str) -> HttpResponse:
    book = get_object_or_404(Book, id=id)
    context = {"book": book}
    return render(request, "books/view.html", context)


@login_required(login_url="/login/")
def update(request: HttpRequest, id: str) -> HttpResponse:
    book = get_object_or_404(Book, id=id)
    template = loader.get_template("books/update.html")
    context = {
        "book": book,
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url="/login/")
def update_record(request: HttpRequest, id: str) -> HttpResponse:
    new_book = request.POST
    book = get_object_or_404(Book, id=id)
    book.topic = new_book.get("topic")
    book.text = new_book.get("text")
    book.author = new_book.get("author")
    book.genre = new_book.get("genre")
    book.last_edit_time = timezone.now()
    book.save()
    return HttpResponseRedirect(reverse("index"))
