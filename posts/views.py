from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from posts.forms import CommonPostForm
from posts.models import Post


# Create your views here.
def hello(request):
    return HttpResponse("Hello Django!")


def main(request):

    return render(request, "base.html")


def about(request):

    return HttpResponse("<h1>About us</h1> <a href='/'>Main</a>")


def get_posts(request):
    post = Post.objects.all()

    return render(request, "posts/posts_view.html", context={"posts": post})


def get_post(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, "posts/post_detail.html", context={"post": post})


def create_post(request: HttpRequest):

    if request.method == "GET":
        form = CommonPostForm()
        return render(request, "posts/create_post.html", context={"form": form})

    if request.method == "POST":
        form = CommonPostForm(request.POST, files=request.FILES)
        if form.is_valid():
            user = request.user
            if user and not isinstance(user, AnonymousUser):
                Post.objects.create(
                    header=form.cleaned_data.get("header"),
                    description=form.cleaned_data.get("description"),
                    rate=form.cleaned_data.get("rate"),
                    is_published=form.cleaned_data.get("is_published"),
                    user=user,
                )
                return redirect("post_list")
            form.add_error(None, "Вы не залогинились!")
        return render(request, "posts/create_post.html", context={"form": form})
