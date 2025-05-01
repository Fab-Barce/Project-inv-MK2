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
        fields = ['categoria_id', 'nombre', 'descripcion','activo']  # Campos de Categoria

class EmpresaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['empresa_id', 'nombre']  # Campos de Empresa

class ProveedorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ['proveedor_id', 'nombre', 'direccion', 'nombre_representante', 'RFC', 'descripcion', 'num_telef','activo']  # Campos de Proveedor

class UsuarioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['user_id', 'nombre', 'rol', 'correo', 'contrasena','activo'] #,'activo' # Campos de Usuario

class OperadorListSerializer(serializers.ModelSerializer):
    empresa = serializers.CharField(source='empresa_id.nombre', read_only=True)
    class Meta:
        model = Operador
        fields = ['operador_id', 'nombre', 'empresa_id', 'empresa','activo']  # Campos de Operador

class VehiculoListSerializer(serializers.ModelSerializer):
    empresa = serializers.CharField(source='empresa_id.nombre', read_only=True)
    operador = serializers.CharField(source='operador_id.nombre', read_only=True)
    class Meta:
        model = Vehiculo
        fields = ['vehiculo_id', 'num_serie', 'placas', 'operador_id', 'imagen_vehi', 'empresa_id', 'marca', 'anio', 'empresa', 'operador','activo','linea', 'num_unidad'] #,'activo' # Campos de Vehiculo

class RefaccionesListSerializer(serializers.ModelSerializer):
    proveedor = serializers.CharField(source='proveedor_id.nombre', read_only=True)
    categoria = serializers.CharField(source='categoria_id.nombre', read_only=True)
    empresa = serializers.CharField(source='empresa_id.nombre', read_only=True)
    class Meta:
        model = Refacciones
        fields = ['refaccion_id', 'proveedor_id', 'vehiculo_id', 'numero_parte', 'nombre', 'cantidad', 'stock_minimo', 'costo', 'categoria_id', 'imagen_refa', 'empresa_id', 'proveedor', 'categoria', 'empresa', 'activo', 'marca'] #,'activo'  # Campos de Refacciones

class MovimientosListSerializer(serializers.ModelSerializer):
    nombre_refaccion = serializers.CharField(source='refaccion_id.nombre', read_only=True)
    placa_vehiculo = serializers.CharField(source='vehiculo_id.placas', read_only=True)
    user_nombre = serializers.CharField(source='user_id.nombre', read_only=True)
    class Meta:
        model = Movimientos
        fields = ['id_movimiento', 'refaccion_id', 'vehiculo_id', 'cantidad', 'fecha', 'hora', 'motivo', 'tipo_movimiento', 'user_id', 'nombre', 'placas', 'nombre_refaccion', 'placa_vehiculo', 'user_nombre']  # Campos de Movimientos



class CategoriaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['categoria_id', 'nombre', 'descripcion','activo']  # Campos de Categoria

class EmpresaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['empresa_id', 'nombre']  # Campos de Empresa

class ProveedorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ['proveedor_id', 'nombre', 'direccion', 'nombre_representante', 'RFC', 'descripcion', 'num_telef','activo']  # Campos de Proveedor

class UsuarioDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['user_id', 'nombre', 'contrasena', 'rol', 'correo','activo']  # Campos de Usuario

class OperadorDetailSerializer(serializers.ModelSerializer):
    empresa = serializers.CharField(source='empresa_id.nombre', read_only=True)
    class Meta:
        model = Operador
        fields = ['operador_id', 'nombre', 'empresa_id', 'empresa','activo']  # Campos de Operador

class VehiculoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['vehiculo_id', 'num_serie', 'placas', 'operador_id', 'imagen_vehi', 'empresa_id', 'marca', 'anio','linea','activo', 'num_unidad']  # Campos de Vehiculo

class RefaccionesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refacciones
        fields = ['refaccion_id', 'proveedor_id', 'vehiculo_id', 'numero_parte', 'nombre', 'cantidad', 'stock_minimo', 'costo', 'categoria_id', 'imagen_refa', 'empresa_id','activo', 'marca']  # Campos de Refacciones

class MovimientosDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimientos
        fields = ['id_movimiento', 'refaccion_id', 'vehiculo_id', 'cantidad', 'fecha', 'motivo', 'tipo_movimiento', 'user_id', 'nombre', 'placas']  # Campos de Movimientos


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['user_id', 'nombre', 'correo', 'rol','activo']

