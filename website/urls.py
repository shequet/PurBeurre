from django.contrib import admin
from django.urls import include, path
from .views import register, profile
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include('purbeurre.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', register, name='register'),
    path('accounts/profile/', profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

