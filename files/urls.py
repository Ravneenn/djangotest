from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings





urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/auth/', include('knox.urls')),
    path('api/auth/', include('members.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('', include('members.urls')),
    path('library/', include('library.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
