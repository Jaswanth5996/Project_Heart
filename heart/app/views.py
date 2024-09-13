from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import logout
from . import models
from django.contrib.auth.decorators import login_required

def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in.")
                return redirect('home')  # Redirect to the admin site or another page
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def HomeView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            models.Contact.objects.create(name=name, email=email, message=message)
            messages.success(request, "Your message has been sent successfully!")
            return redirect('home')
        else:
            messages.error(request, "All fields are required.")

    return render(request, "home.html")

def Logout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def Message(request):
    messages_list = models.Contact.objects.all()
    messages.success(request, "Logged out.")
    return render(request, 'messages.html', {'messages': messages_list})
