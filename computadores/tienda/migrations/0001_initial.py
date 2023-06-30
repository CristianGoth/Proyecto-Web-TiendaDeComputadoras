# Generated by Django 4.2.2 on 2023-06-30 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.BigAutoField(db_column='idCategoria', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('pnombre', models.CharField(max_length=15)),
                ('appaterno', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('contrasena', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.BigAutoField(db_column='idProducto', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('marca', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=200)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('imagen', models.ImageField(null=True, upload_to='productos/')),
                ('id_categoria', models.ForeignKey(db_column='idCategoria', on_delete=django.db.models.deletion.CASCADE, to='tienda.categoria')),
            ],
        ),
    ]
