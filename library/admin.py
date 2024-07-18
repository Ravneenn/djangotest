from django.contrib import admin

from .models import Article, Reporter

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("headline", "reporter", "pub_date", "slug")
    search_fields = ("headline", "content")
    readonly_fields = ("pub_date", "reporter")


admin.site.register(Article, ArticleAdmin)
admin.site.register(Reporter)