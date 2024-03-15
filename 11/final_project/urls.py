"""
URL configuration for final_project project.

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
from django.urls import path , include
from final.views import register , user_login,home,criticismm,menu,criticism_list,create_criticism,delete,update
from django.contrib import admin
urlpatterns = [
    # ... other url patterns
    path('admin/' , admin.site.urls),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path("",home,name="home"),
    path("menu/",menu,name="menu"),
    path("menu/criticism",criticism_list,name="criticism_list"),
    path("menu/criticism/<int:criticism_id>/",criticismm,name="criticism "),
    path("menu/write_criticism/",create_criticism,name="write_criticism"),
    path('delete/<int:criticism_id>',delete,name="delete"),
    path('update/<int:criticism_id>',update,name="update")
]