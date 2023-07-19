from django.shortcuts import render
from django.http import HttpResponse
posts =  [

    {
        'author' : "LeulD",
        'title' : 'Blog Post 1',
        'content': 'First post content',
        'date_posted' : 'August 27, 2018'
    },
    {
        'author' : "DaniD",
        'title' : 'Blog Post 2',
        'content': 'First post content',
        'date_posted' : 'August 27, 2018'
    }
]

def home(req):

    context = {
        
        'posts' : posts
    }
    return render(req , '_blog/home.html', context)

def about(req):
    return render(req , "_blog/about.html")
