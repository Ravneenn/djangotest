from django.contrib import admin

from .models import Article, Reporter, Language

class ArticleAdmin(admin.ModelAdmin):
    list_display = ( "headline","id", "reporter", "pub_date", "slug", )
    search_fields = ("headline", "content")
    readonly_fields = ("pub_date", "reporter")
    list_filter = ("reporter",)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Reporter)
admin.site.register(Language)