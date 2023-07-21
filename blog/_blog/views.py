from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin

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
     
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title' , 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(req):
    return render(req , "_blog/about.html", {"title": "About"})

