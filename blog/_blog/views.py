from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Post

def home(req):

    context = {
        
        'posts' : Post.objects.all()
    }
    return render(req , '_blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = '_blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
     



def about(req):
    return render(req , "_blog/about.html", {"title": "About"})

