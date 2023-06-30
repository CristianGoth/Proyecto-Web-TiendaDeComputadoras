from django.urls import path
from . import views

urlpatterns = [
    #PAGINA PRINCIPAL
    path('', views.index_view, name='index'),
    path('index/', views.index_view, name='index'),
    path('carrito/', views.carrito_view, name='carrito'),
    path('ofertas/', views.ofertas_view, name='ofertas'),
    path('productos/', views.productos_view, name='productos'),
    path('contacto/', views.contacto_view, name='contacto'),
    path('inisesion/', views.inisesion_view, name='inisesion'),
    path('inisesion/registrosesi.html', views.registrosesi_view, name='registrosesi_html'),

    

    #AGREGADO Y ELIMINADO DE PRODUCTO
    path("producto_mod/", views.producto_mod, name="producto_mod"),
    path('producto_find/<int:pk>/', views.producto_find, name='producto_find'),
    path('producto_add/',views.producto_add, name='producto_add'),
    path('producto_del/<int:pk>/', views.producto_del, name='producto_del'),
    path('producto_update/<int:pk>/', views.producto_update, name='producto_update'),


    # Ruta de página no encontrada (404)
    path('index/', views.not_found_view, name='not_found'),
]