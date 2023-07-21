from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .form import UserRegisterForm  , UserUpdateForm , ProfileUpdateForm
# Create your views here.
def register(req):
     if req.method == 'POST':
          form = UserRegisterForm(req.POST)
          if form.is_valid():
               username = form.cleaned_data.get('username')
               messages.success(req , f'Your account has been created! You are now able to log in')
               form.save()
               return redirect('login')
          
     else:
          form = UserRegisterForm()


     
     return render(req, 'users/register.html', {'form': form})

@login_required
def profile(req):

     if req.method == 'POST':
          u_form = UserUpdateForm( req.POST ,instance=req.user)
          p_form = ProfileUpdateForm( req.POST , req.FILES,instance=req.user.profile)

          if u_form.is_valid() and p_form.is_valid():
               u_form.save()
               p_form.save()
               messages.success(req , f'Your account has been updated!')
               return redirect('profile')
     else:
          u_form = UserUpdateForm(instance=req.user)
          p_form = ProfileUpdateForm(instance=req.user.profile)





     context = {"u_form": u_form , 
                "p_form": p_form}
     


     return render(req, 'users/profile.html' , context)
