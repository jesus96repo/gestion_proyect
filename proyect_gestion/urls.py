
from django.contrib import admin
from django.urls import path
from proyect_gestion import views





urlpatterns = [
    path('', views.index, name='index'),
    path('usuarios/login', views.login_view, name='login'),
    path('admin/', admin.site.urls),
    path('usuarios/logout', views.logout_view, name='logout'),
    path('usuarios/registro', views.register, name='register'),
    path('hello_world/', views.hello_world ),
    path("hi/",views.hi)
]
