from django.urls import path
from categorias.views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),

    path('acerca/', acerca, name="acerca"),

    #____ Servicios
    path('servicios/', ServiciosList.as_view(), name="servicios"),    
    path('serviciosCreate/', ServiciosCreate.as_view(), name="serviciosCreate"), 
    path('serviciosUpdate/<int:pk>/', ServiciosUpdate.as_view(), name="serviciosUpdate"), 
    path('serviciosDelete/<int:pk>/', ServiciosDelete.as_view(), name="serviciosDelete"),

    #____ Accesorios
    path('accesorios/', AccesoriosList.as_view(), name="accesorios"),    
    path('accesoriosCreate/', AccesoriosCreate.as_view(), name="accesoriosCreate"), 
    path('accesoriosUpdate/<int:pk>/', AccesoriosUpdate.as_view(), name="accesoriosUpdate"), 
    path('accesoriosDelete/<int:pk>/', AccesoriosDelete.as_view(), name="accesoriosDelete"),

    #____ Clientes
    path('clientes/', ClientesList.as_view(), name="clientes"),    
    path('clientesCreate/', ClientesCreate.as_view(), name="clientesCreate"), 
    path('clientesUpdate/<int:pk>/', ClientesUpdate.as_view(), name="clientesUpdate"), 
    path('clientesDelete/<int:pk>/', ClientesDelete.as_view(), name="clientesDelete"),

    #____ Peluqueros
    path('peluqueros/', PeluquerosList.as_view(), name="peluqueros"),    
    path('peluquerosCreate/', PeluquerosCreate.as_view(), name="peluquerosCreate"), 
    path('peluquerosUpdate/<int:pk>/', PeluquerosUpdate.as_view(), name="peluquerosUpdate"), 
    path('peluquerosDelete/<int:pk>/', PeluquerosDelete.as_view(), name="peluquerosDelete"),

    #___ Login / Logout / Registration
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name="categorias/logout.html"), name="logout"),
    path('registro/', register, name="registro"),

    #___ Buscar
    path('buscarAccesorios/', buscarAccesorios, name="buscarAccesorios"),
    path('encontrarAccesorios/', encontrarAccesorios, name="encontrarAccesorios"),

    #___ Edición de Perfil / Avatar
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiarClave"),
    path('agregarAvatar/', agregarAvatar, name="agregarAvatar"),

]