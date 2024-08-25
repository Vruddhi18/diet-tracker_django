"""
URL configuration for foodie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from counter import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('counter.urls')),
    path('daily/',views.daily,name="daily"),
    path('daily/addfood',views.addfood,name='addfood'),
    path('daily/added/<int:food_id>',views.added,name='added'),
    path('daily/delete/<int:food_id>',views.delete,name='delete'),


]
