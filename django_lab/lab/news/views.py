from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.utils import timezone

from .forms import NewsForm
from .models import News


# Create your views here.
@login_required(login_url="/login/")
def index(request: HttpRequest) -> HttpResponse:
    news = News.objects.order_by("-create_time")
    context = {"news": news}

    return render(request, "news/index.html", context)


@login_required(login_url="/login/")
def add(request: HttpRequest) -> HttpResponse:
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


@login_required(login_url="/login/")
def get(request: HttpRequest, id: str) -> HttpResponse:
    news = get_object_or_404(News, id=id)
    context = {"news": news}
    return render(request, "news/view.html", context)


@login_required(login_url="/login/")
def update(request: HttpRequest, id: str) -> HttpResponse:
    news = get_object_or_404(News, id=id)
    template = loader.get_template("news/update.html")
    context = {
        "news": news,
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url="/login/")
def update_record(request: HttpRequest, id: str) -> HttpResponse:
    new_news = request.POST
    news = get_object_or_404(News, id=id)
    news.topic = new_news.get("topic")
    news.text = new_news.get("text")
    news.author = new_news.get("author")
    news.last_edit_time = timezone.now()
    news.save()
    return HttpResponseRedirect(reverse("index"))


@login_required(login_url="/login/")
def delete(request: HttpRequest, id: str) -> HttpResponse:
    news = get_object_or_404(News, id=id)
    news.delete()
    return render(request, "news/view.html")
