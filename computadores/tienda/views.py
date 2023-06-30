from django.shortcuts import render
from .models import Categoria, Producto, Usuario
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

def index_view(request):
    request.session["usuario"]="lufernandezm"
    usuario = request.session["usuario"]
    context = {"usuario":usuario}
    return render(request,'tienda/index.html',context)

def carrito_view(request):
    return render(request, 'tienda/carrito.html')

def contacto_view(request):
    return render(request, 'tienda/contacto.html')

def productos_view(request):
    prodproductos = Producto.objects.filter(id_categoria="1")
    context = {"productos":prodproductos}
    return render(request,"tienda/productos.html",context)

def ofertas_view(request):
    prodofertas = Producto.objects.filter(id_categoria="2")
    context = {"productos":prodofertas}
    return render(request,"tienda/ofertas.html",context)


def inisesion_view(request):
    return render(request, 'tienda/inisesion.html')

def usuarioAdd(request):
    
    username      = request.POST["username"]
    email         = request.POST["email"]
    name          = request.POST["name"]
    password      = request.POST["password"]
    cellphone     = request.POST["cellphone"]
    
    
    objUser=User.objects.create_user(username   = username,
                                    email       = email,
                                    name        = name,
                                    password    = password,
                                    cellphone   = cellphone)
    
    objUser.save()
    
    return render(request,'tienda/index.html')

def registrosesi_view(request):
    return render(request, 'tienda/registrosesi.html')

@staff_member_required
def producto_add(request):
    if request.method == "POST":
        categoria = request.POST["categoria"]
        nombre = request.POST["nombre"]
        marca = request.POST["marca"]
        descripcion = request.POST["detalle"]
        precio = request.POST["precio"]
        stock = request.POST["stock"]
        imagen = request.POST["imagen"]

        # Validar el campo 'precio'
        if not precio.isnumeric():
            lista_categorias = Categoria.objects.all()
            context = {
                "categorias": lista_categorias,
                "mensaje": "El campo 'precio' debe ser un número válido."
            }
            return render(request, 'tienda/producto_add.html', context)

        objCategoria = Categoria.objects.get(id_categoria=categoria)

        objProducto = Producto.objects.create(
            id_categoria=objCategoria,
            nombre=nombre,
            marca=marca,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            imagen=imagen
        )

        objProducto.save()
        lista_categorias = Categoria.objects.all()
        context = {"mensaje": "Se guardó el producto correctamente."}
        return render(request, 'tienda/producto_add.html', context)

    else:
        lista_categorias = Categoria.objects.all()
        context = {"categorias": lista_categorias}
        return render(request, 'tienda/producto_add.html', context)


@staff_member_required
def producto_mod(request):
    lista_productos = Producto.objects.all()
    context = {"productos":lista_productos}
    return render(request,'tienda/producto_mod.html', context)

@staff_member_required
def producto_del(request,pk):
    try:
        prod = Producto.objects.get(id_producto=pk)
        prod.delete()
        mensaje = "El producto se ha eliminado"
        lista_productos = Producto.objects.all()
        context = {"productos":lista_productos, "mensaje":mensaje}
        return render(request,'tienda/producto_mod.html', context)
    except:
        mensaje = "El producto NO ha sido eliminado"
        lista_productos = Producto.objects.all()
        context = {"productos":lista_productos, "mensaje":mensaje}
        return render(request,'tienda/producto_mod.html', context)

@staff_member_required
def producto_find(request,pk):
    if pk != "":
        producto = Producto.objects.get(id_producto=pk)
        lista_categorias = Categoria.objects.all() 
        
        context = {"producto":producto, "categorias":lista_categorias}
        return render(request,'tienda/productos_edit.html', context)
    else:
        mensaje = "El producto NO existe"
        context = {"mensaje":mensaje}
        return render(request,'tienda/producto_mod.html', context)

@staff_member_required
def producto_update(request, pk):
    try:
        producto = Producto.objects.get(id_producto=pk)
    except Producto.DoesNotExist:
        mensaje = "El producto no existe"
        context = {"mensaje": mensaje}
        return render(request, 'tienda/producto_mod.html', context)

    if request.method == "POST":
        categoria = request.POST["categoria"]
        nombre = request.POST["nombre"]
        marca = request.POST["marca"]
        descripcion = request.POST["detalle"]
        precio = request.POST["precio"]
        stock = request.POST["stock"]

        objCategoria = Categoria.objects.get(id_categoria=categoria)

        producto.id_categoria = objCategoria
        producto.nombre = nombre
        producto.marca = marca
        producto.descripcion = descripcion
        producto.precio = precio
        producto.stock = stock

        producto.save()
        lista_categorias = Categoria.objects.all()
        context = {"mensaje": "El producto se ha actualizado correctamente", "categorias": lista_categorias, "producto": producto}
        return render(request, 'tienda/productos_edit.html', context)
    else:
        lista_categorias = Categoria.objects.all()
        context = {"producto": producto, "categorias": lista_categorias}
        return render(request, 'tienda/productos_edit.html', context)

    
@login_required
def usuario(request):
    request.session["usuario"]="lucasfernandezm"
    usuario = request.session["usuario"] 
    context = {"usuario":usuario}
    return render(request,'venta/usuario.html',context)

def not_found_view(request):
    return render(request, 'tienda/index.html')

