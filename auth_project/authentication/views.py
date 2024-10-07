from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
  if request.methd == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Account created for {username}!')
      return redirect('login')
    else:
      form = UserRegisterForm()
  return render(request, 'authentication/register.html', {'form': form})

def login_view(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('profile')
    else:
      messages.info(request, 'Username or password is incorrect')
  return render(request, 'authentication/login.html')

def logout_view(request):
  logout(request)
  return redirect('login')

@login_required
def profile(request):
  return render(request, 'authentication/profile.html')