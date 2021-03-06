"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from movies import urls as movies_urls #se importa de la app movies las urls con el sobrenombre movies_urls
from users import urls as users_urls
from addresses import urls as address_urls
from groups import urls as groups_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include(movies_urls, namespace='movies')),
    path('users/', include(users_urls, namespace='users')),
    path('addresses/', include(address_urls, namespace='addresses')),
    path('groups/', include(groups_urls, namespace='groups'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
