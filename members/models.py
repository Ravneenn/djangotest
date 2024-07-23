from urllib import request
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.text import slugify
from django.contrib.auth import user_logged_in



# Create your models here.


def default_work_status():
    return WorkStatus.objects.get(name="Yeni Görev")

class Role(models.Model):
    roleName = models.CharField(max_length=50)
    authorizedOn = models.ManyToManyField('members.Role', null=True, blank=True)

    def __str__(self):
        return self.roleName

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password = None, **extra_fields):
        if not email:
            raise ValueError('Email is required')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using= self._db)
        return user

    def create_superuser(self, email, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.CharField(max_length=200, unique=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True)
    objects = CustomUserManager()
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, unique=True, db_index=True, editable = False, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.first_name +" " + self.last_name  
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(args, **kwargs)

class WorkStatus(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(Role, blank=True, on_delete=models.CASCADE , null=True)
    slug = models.SlugField(blank=True, unique=True, db_index=True, editable = False)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(args, **kwargs)

class Work(models.Model):
    name = models.CharField(max_length=200, unique=True)
    deadline = models.DateField()
    appointed = models.ManyToManyField('members.CustomUser', related_name='appointed_works')
    appointer = models.ForeignKey('members.CustomUser',  on_delete=models.CASCADE, related_name='appointer_works')
    status = models.ForeignKey("members.WorkStatus", on_delete=models.CASCADE, default=default_work_status)
    description = models.TextField()
    relatedWork = models.ForeignKey('members.Work',on_delete=models.CASCADE , null=True, blank=True)
    img = models.ImageField(upload_to='workimages')
    slug = models.SlugField(blank=True, unique=True, db_index=True, editable = False)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(args, **kwargs)


