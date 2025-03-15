from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Movimientos(models.Model):
    id_movimiento = models.AutoField(primary_key=True)  # Campo autoincremental
    refaccion_id = models.ForeignKey('Refacciones', on_delete=models.CASCADE, blank=True, null=True)  # Relación con el modelo Refacciones
    vehiculo_id = models.ForeignKey('Vehiculo', on_delete=models.CASCADE, blank=True, null=True)  # Relación con el modelo Vehiculo
    cantidad = models.PositiveIntegerField(blank=True, null=True)  # Cantidad positiva
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha y hora de creación
    motivo = models.CharField(max_length=255, blank=True, null=True)  # Motivo del movimiento
    tipo_movimiento = models.CharField(max_length=50, blank=True, null=True)  # Tipo de movimiento
    user_id = models.ForeignKey('Usuario', on_delete=models.CASCADE, blank=True, null=True)  # Relación con el modelo Usuario 

    def __str__(self):
        return "{} - {}".format(self.motivo)  # Regresa el motivo

class Refacciones(models.Model):
    refaccion_id = models.AutoField(primary_key=True)  # Campo autoincremental
    proveedor_id = models.ForeignKey('Proveedor', on_delete=models.CASCADE, blank=True, null=True)  # Relación con el modelo Proveedor
    vehiculo_id = models.ForeignKey('Vehiculo', on_delete=models.CASCADE, blank=True, null=True)  # Relación con el modelo Vehiculo
    numero_parte = models.CharField(max_length=100, blank=True, null=True)  # Número de parte
    nombre = models.CharField(max_length=255, blank=True, null=True)  # Nombre de la refacción
    cantidad = models.PositiveIntegerField(blank=True, null=True)  # Cantidad positiva
    sock_minimo = models.PositiveIntegerField(blank=True, null=True)  # Stock mínimo
    costo = models.PositiveIntegerField(blank=True, null=True)  # Costo de la refacción
    categoria_id = models.ForeignKey('Categoria', on_delete=models.CASCADE, blank=True, null=True)  # Relación con el modelo Categoria
    imagen_refa = models.ImageField(upload_to='imagenes_refacciones/', blank=True, null=True)  # Imagen de la refacción
    empresa_id = models.ForeignKey('Empresa', on_delete=models.CASCADE, blank=True, null=True)  # Relación con el modelo Empresa

    def __str__(self):
        return "{}".format(self.nombre)  # Regresa el nombre

class Vehiculo(models.Model):
    vehiculo_id = models.AutoField(primary_key=True)  # Campo autoincremental
    num_serie = models.CharField(max_length=100, blank=True, null=True)  # Número de serie
    placas = models.CharField(max_length=50, blank=True, null=True)  # Placas del vehículo
    operador_id = models.ForeignKey('Operador', on_delete=models.CASCADE, blank=True, null=True)  # Relación con el modelo Operador
    imagen_vehi = models.ImageField(upload_to='imagenes_vehiculos/', blank=True, null=True)  # Imagen del vehículo
    empresa_id = models.ForeignKey('Empresa', on_delete=models.CASCADE, blank=True, null=True)  # Relación con el modelo Empresa
    marca = models.CharField(max_length=100, blank=True, null=True)  # Marca del vehículo
    anio = models.IntegerField(blank=True, null=True)  # Año del vehículo

    def __str__(self):
        return "{}".format(self.num_serie)  # Regresa el número de serie del vehículo

class Usuario(models.Model):
    user_id = models.AutoField(primary_key=True)  # Campo autoincremental
    nombre = models.CharField(max_length=255, blank=True, null=True)  # Nombre del usuario
    contrasena = models.CharField(max_length=255, blank=True, null=True)  # Contraseña del usuario
    rol = models.CharField(max_length=50, blank=True, null=True)  # Rol del usuario
    correo = models.CharField(max_length=50, blank=True, null=True) 

    
    def __str__(self):
        return "{}".format(self.nombre)  # Regresa el nombre del usuario

class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)  # Campo autoincremental
    nombre = models.CharField(max_length=255, blank=True, null=True)  # Nombre de la categoría
    descripcion = models.TextField(blank=True, null=True)  # Descripción de la categoría

    def __str__(self):
        return "{}".format(self.nombre)  # Regresa el nombre de la categoría

class Proveedor(models.Model):
    proveedor_id = models.AutoField(primary_key=True)  # Campo autoincremental
    nombre = models.CharField(max_length=255, blank=True, null=True)  # Nombre del proveedor
    direccion = models.CharField(max_length=255, blank=True, null=True)  # Dirección del proveedor

    def __str__(self):
        return "{}".format(self.nombre)  # Regresa el nombre del proveedor

class Operador(models.Model):
    operador_id = models.AutoField(primary_key=True)  # Campo autoincremental
    nombre = models.CharField(max_length=255, blank=True, null=True)  # Nombre del operador
    empresa_id = models.ForeignKey('Empresa', on_delete=models.CASCADE, blank=True, null=True)  # Relación con el modelo Empresa

    def __str__(self):
        return "{}".format(self.nombre)  # Regresa el nombre del operador

class Empresa(models.Model):
    empresa_id = models.AutoField(primary_key=True)  # Campo autoincremental
    nombre = models.CharField(max_length=255, blank=True, null=True)  # Nombre de la empresa

    def __str__(self):
        return "{}".format(self.nombre)  # Regresa el nombre de la empresa