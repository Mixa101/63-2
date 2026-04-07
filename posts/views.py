from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from posts.forms import PostForm
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
        form = PostForm()
        return render(request, "posts/create_post.html", context={"form": form})

    if request.method == "POST":
        form = PostForm(request.POST, files=request.FILES)
        form.is_valid()
        form.save()
        return redirect("post_list")
