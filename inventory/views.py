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
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

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


class CustomAuthToken(APIView):
    def post(self, request, *args, **kwargs):
        # Obtén los datos enviados en el POST (correo y contraseña)
        correo = request.data.get('correo')
        password = request.data.get('password')

        if not correo or not password:
            return Response({"detail": "Both 'correo' and 'password' are required."},
                             status=status.HTTP_400_BAD_REQUEST)

        # Busca al usuario por correo
        try:
            user = Usuario.objects.get(correo=correo)
        except Usuario.DoesNotExist:
            return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

        # Verifica la contraseña
        if user.contrasena == password:  # Asegúrate de cifrar las contraseñas en producción
            return Response({
                'token': 'tu_token_aqui',  # Genera y devuelve el token si la autenticación fue exitosa
                'user_id': user.user_id,
                'nombre': user.nombre,
                'rol': user.rol
            }, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
        

class CrearUsuarioView(APIView):
    def post(self, request):
        nombre = request.data.get('nombre')
        contrasena = request.data.get('contrasena')
        correo = request.data.get('correo')
        rol = request.data.get('rol')

        if not nombre or not contrasena or not correo:
            return Response({"detail": "Todos los campos son obligatorios."}, status=status.HTTP_400_BAD_REQUEST)

        # Crear usuario con contraseña cifrada
        usuario = Usuario.objects.create(
            nombre=nombre,
            contrasena=contrasena,
            correo=correo,
            rol=rol
        )

        return Response({
            "detail": "Usuario creado correctamente",
            "user_id": usuario.user_id
        }, status=status.HTTP_201_CREATED)
    

class ListaUsuariosView(APIView):
    # ✅ Agregar el método GET para obtener la lista de usuarios
    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioListSerializer(usuarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # ✅ Agregar el método POST para crear un nuevo usuario
    def post(self, request):
        serializer = UsuarioListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

 
    

class UsuarioDetalleView(APIView):
    def delete(self, request, id):
        try:
            usuario = Usuario.objects.get(user_id=id)
            usuario.delete()
            return Response({"detail": "Usuario eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)
        except Usuario.DoesNotExist:
            return Response({"detail": "Usuario no encontrado."}, status=status.HTTP_404_NOT_FOUND)

class UsuarioRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = "user_id"
    queryset = Usuario.objects.all()
    serializer_class = UsuarioDetailSerializer
