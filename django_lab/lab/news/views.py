from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import News
from .forms import NewsForm
from django.utils import timezone


# Create your views here.
def view_news(request: HttpRequest) -> HttpResponse:
    news = News.objects.order_by("-create_time")
    context = {"news": news}

    return render(request, "news/index.html", context)


def add(request):
    if request.method == "POST":
        news = NewsForm(request.POST)

        if news.is_valid():
            news = news.save(commit=False)

            news.create_time = timezone.now()
            news.last_edit_time = timezone.now()
            news.save()
            return redirect("view_news")
        else:
            context = {"form": news}
            return render(request, "news/add.html", context)
    else:
        news = NewsForm()
        context = {"form": news}
        return render(request, "news/add.html", context)
