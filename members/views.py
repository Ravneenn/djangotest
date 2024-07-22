from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import messages
from members.models import CustomUser
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from django.contrib.auth import login, authenticate
from members.models import *
from .forms import WorkForm
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name')

def error_403_view(request, exception=None):
    return render(request, 'errors/403.html', status=403)

def superuser_required(view_func):
    decorated_view_func = user_passes_test(lambda u: u.is_superuser, login_url='/403/')(view_func)
    return decorated_view_func

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

def works(request):
    context = {
        "works": Work.objects.all()
    }
    return render(request, 'dynamic/works.html', context)

def work(request, workName):
    context = {
        "work": Work.objects.get(slug = workName)
    }
    return render(request, 'dynamic/work.html', context)

@superuser_required

def createWork(request, ):
    if request.method == 'POST':
        form = WorkForm(request.POST, request.FILES)
        if form.is_valid():
            work = form.save(commit=False)
            work.appointer = request.user
            work.save()
            form.save_m2m()
            return redirect('work', workName = work.slug)
    else:
        form = WorkForm()
    
    return render(request, '_static/createWork.html', {'form': form})












class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])
        if user is not None:
            login(request, user)
            return Response({
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": AuthToken.objects.create(user)[1]
            })
        return Response({"error": "Invalid credentials"}, status=400)

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user