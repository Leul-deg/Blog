from django.shortcuts import render, redirect
from django.contrib import messages
from .form import UserRegisterForm
# Create your views here.
def register(req):
     if req.method == 'POST':
          form = UserRegisterForm(req.POST)
          if form.is_valid():
               username = form.cleaned_data.get('username')
               messages.success(req , f'Account created for {username}!')
               # form.save()
               return redirect('blog-home')
          
     else:
          form = UserRegisterForm()


     
     return render(req, 'users/register.html', {'form': form})
