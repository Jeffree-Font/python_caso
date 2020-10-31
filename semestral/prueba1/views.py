from django.shortcuts import render,redirect
from .models import Cliente,Insumos,SliderHindex,Galeria,MisionVision

#from django.contrib.auth.models import ContentType
#Para el login

#Utilizamos la tabla de Usuarios 
from django.contrib.auth.models import User
#Usamos la librería de autheticated
from django.contrib.auth import authenticate,logout,login as login_autent
#Uso de un decorador para impedir el acceso a las páginas 
from django.contrib.auth.decorators import login_required

# Create your views here.

def logout_vista(request):
    logout(request)
    return render(request,'core/login.html')

def login(request):
    if request.POST:
        usuario = request.POST.get("nombrex")
        password = request.POST.get("password")
        us = authenticate(request, username=usuario,password=password)
        if us is not None and us.is_active:
            login_autent(request,us)
            return render(request,'core/hindex.html',{'user':us})
        else:
            return render(request,'core/login.html',{'msg':'usuario / contraseña inválida'})
    return render(request,'core/login.html')



def hindex(request):
    autos = SliderHindex.objects.all()
    return render(request,'core/hindex.html',{'autos':autos})


def galeria(request):
    return render(request,'core/galeria.html')

def mision_vision(request):
    mision = MisionVision.objects.all()
    return render(request,'core/mision_vision.html',{'mision':mision})


def direccion(request):
    return render(request,'core/direccion.html')


def registro(request):
    if request.POST:
        nombre= request.POST.get("txtNombre")
        apellido= request.POST.get("txtApellido")
        email= request.POST.get("txtEmail")
        username= request.POST.get("txtUsuario")
        password= request.POST.get("txtpassword")
        password2= request.POST.get("txtpassword2")
        try:
            u=User.objects.get(username=username)
            mensaje="Usuario ya existe"
            return render(request,'core/registro.html',{'msg':mensaje})
        except:
            if password != password2:
                mensaje="contraseñas invalidas"
                return render(request,'core/registro.html',{'msg':mensaje})
            
        u = User()
        u.first_name=nombre
        u.last_name=apellido
        u.username=username
        u.email=email
        u.set_password(password)
        u.save()
        us = authenticate(request, username=username,password=password)
        login_autent(request,us)
        return render(request,'core/hindex.html',{'user':us})        

    return render(request,'core/registro.html')

def registro_insumo(request):
    insumo = Insumos.objects.all()

    if request.POST:
        nombre = request.POST.get("txtInsumo")
        precio = request.POST.get("txtPrecio")
        descripcion = request.POST.get("txtDescrip")
        stock = request.POST.get("txtStock")
        insu = Insumos(
            name=nombre,
            precio=precio,
            descripcion=descripcion,
            stock=stock
        )
        insu.save()
        return render(request,'core/registro_insumo.html',{'mensaje':'Insumo grabado'})
    return render(request,'core/registro_insumo.html')



def admin_insumos(request):
    insumo = Insumos.objects.all()

    if request.POST:

        accion = request.POST.get("accion")
        if accion == "actualizar":
            nombre = request.POST.get("txtInsumo")
            precio = request.POST.get("txtPrecio")
            descripcion = request.POST.get("txtDescrip")
            stock = request.POST.get("txtStock")
            try:
                insu = Insumos.objects.get(name=nombre)
                insu.stock=stock
                insu.precio=precio
                insu.descripcion=descripcion
                insu.save()
                mensaje="Insumo Actualizado"
            except:
                mensaje="Insumo no actualizado"
            return render(request,'core/admin_insumos.html',{'mensaje':mensaje})

        if accion == "eliminar":
            nombre = request.POST.get("txtInsumo")
            try:
                i = Insumos.object.get(name=nombre)
                i.delete()
                mensaje="Insumo Eliminado"
            except:
                mensaje="Insumo no encontrado"
            return render(request,'core/admin_insumos.html',{'mensaje':mensaje})

        if accion == "registar":

            nombre = request.POST.get("txtInsumo")
            precio = request.POST.get("txtPrecio")
            descripcion = request.POST.get("txtDescrip")
            stock = request.POST.get("txtStock")
            insu = Insumos(
                name=nombre,
                precio=precio,
                descripcion=descripcion,
                stock=stock
            )
            insu.save()
            return render(request,'core/admin_insumos.html',{'mensaje':'Insumo grabado'})
            
    return render(request,'core/admin_insumos.html')
