"""Demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from DemoApp.views import beer, champagne, details, logIn, logOut, profile, signUp, temp, vodka, wine

# Django admin header customization

admin.site.site_header = "D-Drink Admin Pannel"
admin.site.site_title = "WellCome to D-Drink Dashboard"
admin.site.index_title = "Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wine/', wine, name='wine'),
    path('vodka/', vodka, name='vodka'),
    path('champagne/', champagne, name='champagne'),
    path('beer/', beer, name='beer'),
    path('', temp, name='home'),
    path('detail/<int:product_id>/<str:product_name>', details, name='details'),
    path('signUp/',signUp),
    path('logIn/',logIn),
    path('logOut/',logOut),
    path('profile/',profile, name='profile')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
