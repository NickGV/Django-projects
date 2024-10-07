from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
  return render(request, 'base.html')

def register(request):
  if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('home')  # Redirige al home después de registrarse
  else:
        form = UserCreationForm()
  return render(request, 'register.html', {'form': form})

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
  return render(request, 'login.html')

def logout_view(request):
  logout(request)
  return redirect('login')

@login_required
def profile(request):
  return render(request, 'profile.html')