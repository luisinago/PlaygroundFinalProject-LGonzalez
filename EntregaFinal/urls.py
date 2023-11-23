from django.contrib import admin
from django.urls import path, include

#Para imagen de Perfil
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('', include('Personajes.urls')),
    path('', include('Accounts.urls')),
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
