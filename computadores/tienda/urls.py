from django.urls import path
from . import views

urlpatterns = [
    ##PAGINA PRINCIPAL
    path('',views.index_view,name=''),
    path('index/',views.index_view,name='index'),
    path('carrito/',views.carrito_view,name='carrito'),
    path('ofertas/',views.ofertas_view,name='ofertas'),
    path('productos/',views.productos_view,name='productos'),
    path('registrosesi/',views.registrosesi_view,name='registrosesi'),
    path('contacto/',views.contacto_view,name='contacto'),
    path('inisesion/',views.inisesion_view,name='inisesion'),

    ##AGREGADO Y ELIMINADO DE PRODUCTO
    
    path("producto_mod/", views.producto_mod, name="producto_mod"),

]