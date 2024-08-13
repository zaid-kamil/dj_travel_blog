from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def logout_view(request):
    return redirect('index')