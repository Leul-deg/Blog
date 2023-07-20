from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def register(req):
     form = UserCreationForm()
     return render(req, 'users/register.html', {'form': form})

