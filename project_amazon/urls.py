"""
URL configuration for project_amazon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/',registration,name='registration'),
    path('home/',home,name='home'),
    path('user_login/',user_login,name='user_login'),
    path('reset_password/',reset_password,name='reset_password'),
    path('user_logout/',user_logout,name='user_logout'),
    path('display_details/',display_details,name='display_details'),
    path('change_password/',change_password,name='change_password'),
    path('mobiles/',mobiles,name='mobiles'),
    path('today_deals/',today_deals,name='today_deals'),
    path('amazon_mini_tv/',amazon_mini_tv,name='amazon_mini_tv'),
    path('Homee/',Homee,name='Homee'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
