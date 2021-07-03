from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register (req) :
  if req.method == 'POST' :
    form = UserCreationForm(req.POST)
    if form.is_valid() : 
      form.save()
      user = form.cleaned_data.get('username')
      messages.success(req, f"Created user for {user}")
      return redirect('user-login')
  else :
    form = UserCreationForm()

  return render(req, 'users/register.html', {
    'form' : form
  })

def user (req, id) : 
  return render(req, 'users/user.html', {
    'user' : User.objects.get(id=id)
  })

@login_required
def me (req) :
  return render(req, 'users/me.html')