"""LibrarySystem URL Configuration

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
from library import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('signup/',views.usersignup,name="signup"),
    path('login/',views.userlogin,name="login"),
    path('profile/',views.userprofile,name = "profile"),
    path('logout/',views.userlogout,name ="logout"),
    path('bookadd/',views.addbook,name ="addbook"),
    path('bookadd/<int:id>',views.updatebook,name ="updatebook"),
    path('guests/',views.guests,name ="guests"),
    
]
