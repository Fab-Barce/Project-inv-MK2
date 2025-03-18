from rest_framework import serializers
from .models import Categoria
from .models import Empresa
from .models import Proveedor
from .models import Usuario
from .models import Operador
from .models import Vehiculo
from .models import Refacciones
from .models import Movimientos

class CategoriaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['categoria_id', 'nombre', 'descripcion']  # Campos de Categoria

class EmpresaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['empresa_id', 'nombre']  # Campos de Empresa

class ProveedorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ['proveedor_id', 'nombre', 'direccion']  # Campos de Proveedor

class UsuarioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['user_id', 'nombre', 'rol', 'correo']  # Campos de Usuario

class OperadorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operador
        fields = ['operador_id', 'nombre']  # Campos de Operador

class VehiculoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['vehiculo_id', 'num_serie', 'placas', 'marca', 'anio']  # Campos de Vehiculo

class RefaccionesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refacciones
        fields = ['refaccion_id', 'nombre', 'costo']  # Campos de Refacciones

class MovimientosListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimientos
        fields = ['id_movimiento', 'refaccion_id', 'vehiculo_id', 'cantidad', 'fecha', 'motivo', 'tipo_movimiento', 'user_id']  # Campos de Movimientos



class CategoriaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['categoria_id', 'nombre', 'descripcion']  # Campos de Categoria

class EmpresaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['empresa_id', 'nombre']  # Campos de Empresa

class ProveedorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ['proveedor_id', 'nombre', 'direccion']  # Campos de Proveedor

class UsuarioDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['user_id', 'nombre', 'contrasena', 'rol', 'correo']  # Campos de Usuario

class OperadorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operador
        fields = ['operador_id', 'nombre', 'empresa_id']  # Campos de Operador

class VehiculoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['vehiculo_id', 'num_serie', 'placas', 'operador_id', 'imagen_vehi', 'empresa_id', 'marca', 'anio']  # Campos de Vehiculo

class RefaccionesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refacciones
        fields = ['refaccion_id', 'proveedor_id', 'vehiculo_id', 'numero_parte', 'nombre', 'cantidad', 'sock_minimo', 'costo', 'categoria_id', 'imagen_refa', 'empresa_id']  # Campos de Refacciones

class MovimientosDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimientos
        fields = ['id_movimiento', 'refaccion_id', 'vehiculo_id', 'cantidad', 'fecha', 'motivo', 'tipo_movimiento', 'user_id']  # Campos de Movimientos


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['user_id', 'nombre', 'correo', 'rol']
# ... existing code ...

