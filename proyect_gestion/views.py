from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

from .forms import RegisterForm

"""
Nos permite utilizar los templates
"""

def index(request):
    return render(request, 'index.html', {
        #context
        
        'title' : 'Lista de Producto:',
        'message': 'Listado de productos',
        'productos': [
            {'title':'Aluminio','precio':20,'stock': True},
            {'title':'Bronce','precio':15,'stock': True},
            {'title':'Mercurio','precio':35,'stock': False},
        ]
        
    })


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Hi, current server time is {now}'.format(now= str(now) ))



def hi(request):

    import pdb; pdb.set_trace()
    return HttpResponse('Hi')


def login_view(request):


    if  request.method == 'POST':
        username = request.POST.get('username') #diccionario
        password = request.POST.get('password')

        user = authenticate(username = username, password= password) #si no hay sale un none

        if user: 
            login(request, user)
            messages.success(request, 'Bienvenido Usuario'.format(user.username))


            #Nos redirecciona al index
            return redirect('index')

        else:
            messages.error(request, 'Usuario o contraseña no valido')
        
    #print(username)
    #print(password)
    return render(request, 'users/login.html')



def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada exitosamente')

    return redirect('login')


def register(request):
    form = RegisterForm()
    return render(request, 'user/register.html',{
        'form': form

    })



