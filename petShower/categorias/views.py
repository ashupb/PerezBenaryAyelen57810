from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "categorias/index.html")

def acerca(request):
    return render(request, "categorias/acerca.html")

#___ Servicios
class ServiciosList(ListView, LoginRequiredMixin):
    model = Servicios

class ServiciosCreate(CreateView, LoginRequiredMixin):
    model = Servicios
    fields = ["nombre", "tamanio_mascota", "valor"]
    success_url = reverse_lazy("servicios")

class ServiciosUpdate(UpdateView, LoginRequiredMixin):
    model = Servicios
    fields = ["nombre", "tamanio_mascota", "valor"]
    success_url = reverse_lazy("servicios")

class ServiciosDelete(DeleteView, LoginRequiredMixin):
    model = Servicios
    success_url = reverse_lazy("servicios")


#___ Accesorios
class AccesoriosList(ListView, LoginRequiredMixin):
    model = Accesorios

class AccesoriosCreate(CreateView, LoginRequiredMixin):
    model = Accesorios
    fields = ["nombre", "valor"]
    success_url = reverse_lazy("accesorios")

class AccesoriosUpdate(UpdateView, LoginRequiredMixin):
    model = Accesorios
    fields = ["nombre", "valor"]
    success_url = reverse_lazy("accesorios")

class AccesoriosDelete(DeleteView, LoginRequiredMixin):
    model = Accesorios
    success_url = reverse_lazy("accesorios")

#___ Clientes
class ClientesList(ListView, LoginRequiredMixin):
    model = Clientes

class ClientesCreate(CreateView):
    model = Clientes
    fields = ["nombre", "apellido", "email", "nombre_mascota"]
    success_url = reverse_lazy("clientes")

class ClientesUpdate(UpdateView, LoginRequiredMixin):
    model = Clientes
    fields = ["nombre", "apellido", "email", "nombre_mascota"]
    success_url = reverse_lazy("clientes")

class ClientesDelete(DeleteView, LoginRequiredMixin):
    model = Clientes
    success_url = reverse_lazy("clientes")

#___ Peluqueros
class PeluquerosList(ListView, LoginRequiredMixin):
    model = Peluqueros

class PeluquerosCreate(CreateView, LoginRequiredMixin):
    model = Peluqueros
    fields = ["nombre", "apellido"]
    success_url = reverse_lazy("peluqueros")

class PeluquerosUpdate(UpdateView, LoginRequiredMixin):
    model = Peluqueros
    fields = ["nombre", "apellido"]
    success_url = reverse_lazy("peluqueros")

class PeluquerosDelete(DeleteView, LoginRequiredMixin):
    model = Peluqueros
    success_url = reverse_lazy("peluqueros")

# ___ Login / Logout / Registration

def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            #_______ Buscar Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            #______________________________________________________________
            return render(request, "categorias/index.html")
        else:
            return redirect(reverse_lazy('login'))
        
    else:
        miForm = AuthenticationForm()

    return render(request, "categorias/login.html", {"form": miForm})


def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()

    return render(request, "categorias/registro.html", {"form": miForm})    

#___ Buscar
@login_required
def buscarAccesorios(request):
    return render(request, "categorias/buscarAccesorios.html")

@login_required
def encontrarAccesorios(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        accesorios = Accesorios.objects.filter(nombre__icontains=patron)
        contexto = {'accesorios': accesorios}    
    else:
        contexto = {'accesorios': Accesorios.objects.all()}
        
    return render(request, "categorias/accesorios.html", contexto)

# ____ Edición de Perfil / Avatar

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("home"))
    else:
        miForm = UserEditForm(instance=usuario)
    return render(request, "categorias/editarPerfil.html", {"form": miForm})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "categorias/cambiar_clave.html"
    success_url = reverse_lazy("home")

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            #_________ Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #__________________________________________
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()

            #_________ Enviar la imagen al home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            #____________________________________________________
            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm()
    return render(request, "categorias/agregarAvatar.html", {"form": miForm})    
    

