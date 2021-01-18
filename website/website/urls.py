from django.contrib import admin
from django.urls import include, path
from .views import register, profile


urlpatterns = [
    path('', include('purbeurre.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', register, name='register'),
    path('accounts/profile/', profile, name='profile'),
]
