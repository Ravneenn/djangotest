from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import messages

from members.models import CustomUser

# Create your views here.


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')



def home(request):
    context = {}
    return render(request, 'dynamic/home.html', context)

def login_user(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, ('Giriş Başarılı'))
            return redirect('home')
        else:
            messages.success(request, ('Hata Olustu'))
            return redirect('login')

    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Kayıt Başarılı')
                return redirect('home')
            else:
                messages.error(request, 'Giriş yapılamadı. Lütfen bilgilerinizi kontrol edin.')
        else:
            messages.error(request, 'Geçersiz form. Lütfen bilgilerinizi kontrol edin.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'authenticate/register_user.html', {"form": form})