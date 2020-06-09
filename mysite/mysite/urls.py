"""mysite URL Configuration

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
from django.urls import path
from django.urls import include
from django.contrib.auth import views as auth_view
from django.conf.urls import url

urlpatterns = [
    url('admin/', admin.site.urls),
    url('',include('blog.urls')),
    url('accounts/login/$',auth_view.LoginView.as_view(),name='login'),
    url('accounts/logout/$',auth_view.LogoutView.as_view(),name='logout',kwargs={'next_page':'/'}),
    
]
'''
url('accounts/login/$',views.login,name='login.html'),
    url('accounts/logout/$',views.logout,name='logout',kwargs={'next_page':'/'}),
'''