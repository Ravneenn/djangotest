from django.db import models
from django.utils.text import slugify

class Reporter(models.Model):
    full_name = models.CharField(max_length= 80)
    avatar = models.ImageField(upload_to="reporter")
    slug = models.SlugField(blank=True, unique=True, db_index=True, editable = False)

    def __str__(self):
        return self.full_name
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.full_name)
        super().save(args, **kwargs)

class Language(models.Model):
    lang_sc = models.CharField(max_length=7)
    lang_name = models.CharField(max_length=20)

    def __str__(self):
        return self.lang_sc




class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True, db_index=True, editable = False)
    langs = models.ManyToManyField(Language)

    def __str__(self):
        return self.headline
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.headline)
        super().save(args, **kwargs)

