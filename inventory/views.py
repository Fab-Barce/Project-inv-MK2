from django.shortcuts import render
from rest_framework import generics
from .models import Categoria
from .serializers import CategoriaListSerializer
from .serializers import CategoriaDetailSerializer
from .models import Empresa
from .serializers import EmpresaListSerializer
from .serializers import EmpresaDetailSerializer
from .models import Proveedor
from .serializers import ProveedorListSerializer
from .serializers import ProveedorDetailSerializer
from .models import Usuario
from .serializers import UsuarioListSerializer
from .serializers import UsuarioDetailSerializer
from .models import Operador
from .serializers import OperadorListSerializer
from .serializers import OperadorDetailSerializer
from .models import Vehiculo
from .serializers import VehiculoListSerializer
from .serializers import VehiculoDetailSerializer
from .models import Refacciones
from .serializers import RefaccionesListSerializer
from .serializers import RefaccionesDetailSerializer
from .models import Movimientos
from .serializers import MovimientosListSerializer
from .serializers import MovimientosDetailSerializer


# Create your views here.
class CategoriaListAPIView(generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaListSerializer
    
class EmpresaListAPIView(generics.ListAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaListSerializer

class ProveedorListAPIView(generics.ListAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorListSerializer

class UsuarioListAPIView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioListSerializer

class OperadorListAPIView(generics.ListAPIView):
    queryset = Operador.objects.all()
    serializer_class = OperadorListSerializer

class VehiculoListAPIView(generics.ListAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoListSerializer

class RefaccionesListAPIView(generics.ListAPIView):
    queryset = Refacciones.objects.all()
    serializer_class = RefaccionesListSerializer

class MovimientosListAPIView(generics.ListAPIView):
    queryset = Movimientos.objects.all()
    serializer_class = MovimientosListSerializer




    
#-----------------------------Para Categorias-----------------------------------#

class CategoriaRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "categoria_id"
    queryset = Categoria.objects.all()
    serializer_class = CategoriaDetailSerializer

class CategoriaCreateAPIView(generics.CreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaDetailSerializer

class CategoriaRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = "categoria_id"
    queryset = Categoria.objects.all()
    serializer_class = CategoriaDetailSerializer
    
class CategoriaDestroyAPIView(generics.DestroyAPIView):
    lookup_field = "categoria_id"
    queryset = Categoria.objects.all()

#---------------------------Para Empresa-------------------------------------#

class EmpresaRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "empresa_id"
    queryset = Empresa.objects.all()
    serializer_class = EmpresaDetailSerializer

class EmpresaCreateAPIView(generics.CreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaDetailSerializer

class EmpresaRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = "empresa_id"
    queryset = Empresa.objects.all()
    serializer_class = EmpresaDetailSerializer

class EmpresaDestroyAPIView(generics.DestroyAPIView):
    lookup_field = "empresa_id"
    queryset = Empresa.objects.all()

#-------------------------Para proveeedor---------------------------------------#

class ProveedorRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "proveedor_id"
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorDetailSerializer

class ProveedorCreateAPIView(generics.CreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorDetailSerializer

class ProveedorRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = "proveedor_id"
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorDetailSerializer

class ProveedorDestroyAPIView(generics.DestroyAPIView):
    lookup_field = "proveedor_id"
    queryset = Proveedor.objects.all()

#-------------------------Para usuarios---------------------------------------#

class UsuarioRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "usuario_id"
    queryset = Usuario.objects.all()
    serializer_class = UsuarioDetailSerializer

class UsuarioCreateAPIView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioDetailSerializer

class UsuarioRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = "usuario_id"
    queryset = Usuario.objects.all()
    serializer_class = UsuarioDetailSerializer

class UsuarioDestroyAPIView(generics.DestroyAPIView):
    lookup_field = "usuario_id"
    queryset = Usuario.objects.all()

#------------------------aPara operadores----------------------------------------#

class OperadorRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "operador_id"
    queryset = Operador.objects.all()
    serializer_class = OperadorDetailSerializer

class OperadorCreateAPIView(generics.CreateAPIView):
    queryset = Operador.objects.all()
    serializer_class = OperadorDetailSerializer

class OperadorRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = "operador_id"
    queryset = Operador.objects.all()
    serializer_class = OperadorDetailSerializer

class OperadorDestroyAPIView(generics.DestroyAPIView):
    lookup_field = "operador_id"
    queryset = Operador.objects.all()

#------------------------para vehiculos----------------------------------------#

class VehiculoRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "vehiculo_id"
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoDetailSerializer

class VehiculoCreateAPIView(generics.CreateAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoDetailSerializer

class VehiculoRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = "vehiculo_id"
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoDetailSerializer

class VehiculoDestroyAPIView(generics.DestroyAPIView):
    lookup_field = "vehiculo_id"
    queryset = Vehiculo.objects.all()

#------------------------Para refacciones----------------------------------------#

class RefaccionesRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "refaccion_id"
    queryset = Refacciones.objects.all()
    serializer_class = RefaccionesDetailSerializer

class RefaccionesCreateAPIView(generics.CreateAPIView):
    queryset = Refacciones.objects.all()
    serializer_class = RefaccionesDetailSerializer

class RefaccionesRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = "refaccion_id"
    queryset = Refacciones.objects.all()
    serializer_class = RefaccionesDetailSerializer

class RefaccionesDestroyAPIView(generics.DestroyAPIView):
    lookup_field = "refaccion_id"
    queryset = Refacciones.objects.all()

#-----------------------Para movimientos-----------------------------------------#

class MovimientosRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "id_movimiento"
    queryset = Movimientos.objects.all()
    serializer_class = MovimientosDetailSerializer

class MovimientosCreateAPIView(generics.CreateAPIView):
    queryset = Movimientos.objects.all()
    serializer_class = MovimientosDetailSerializer

class MovimientosRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = "id_movimiento"
    queryset = Movimientos.objects.all()
    serializer_class = MovimientosDetailSerializer

class MovimientosDestroyAPIView(generics.DestroyAPIView):
    lookup_field = "id_movimiento"
    queryset = Movimientos.objects.all()

