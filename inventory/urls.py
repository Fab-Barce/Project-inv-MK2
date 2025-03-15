from django.urls import path
from . import views

urlpatterns = [
    # Rutas para Categorias
    path("Categorias/", views.CategoriaListAPIView.as_view(), name="lista_categoria"),
    path("Categorias/<int:categoria_id>/", views.CategoriaRetrieveAPIView.as_view(), name="detail_categoria"),
    path("Categorias/create/", views.CategoriaCreateAPIView.as_view(), name="create_categoria"),
    path("Categorias/update/<int:categoria_id>/", views.CategoriaRetrieveUpdateAPIView.as_view(), name="update_categoria"),
    path("Categorias/delete/<int:categoria_id>/", views.CategoriaDestroyAPIView.as_view(), name="delete_categoria"),

    # Rutas para Empresas
    path("Empresas/", views.EmpresaListAPIView.as_view(), name="lista_empresa"),
    path("Empresas/<int:empresa_id>/", views.EmpresaRetrieveAPIView.as_view(), name="detail_empresa"),
    path("Empresas/create/", views.EmpresaCreateAPIView.as_view(), name="create_empresa"),
    path("Empresas/update/<int:empresa_id>/", views.EmpresaRetrieveUpdateAPIView.as_view(), name="update_empresa"),
    path("Empresas/delete/<int:empresa_id>/", views.EmpresaDestroyAPIView.as_view(), name="delete_empresa"),

    # Rutas para Proveedores
    path("Proveedores/", views.ProveedorListAPIView.as_view(), name="lista_proveedor"),
    path("Proveedores/<int:proveedor_id>/", views.ProveedorRetrieveAPIView.as_view(), name="detail_proveedor"),
    path("Proveedores/create/", views.ProveedorCreateAPIView.as_view(), name="create_proveedor"),
    path("Proveedores/update/<int:proveedor_id>/", views.ProveedorRetrieveUpdateAPIView.as_view(), name="update_proveedor"),
    path("Proveedores/delete/<int:proveedor_id>/", views.ProveedorDestroyAPIView.as_view(), name="delete_proveedor"),

    # Rutas para Usuarios
    path("Usuarios/", views.UsuarioListAPIView.as_view(), name="lista_usuario"),
    path("Usuarios/<int:usuario_id>/", views.UsuarioRetrieveAPIView.as_view(), name="detail_usuario"),
    path("Usuarios/create/", views.UsuarioCreateAPIView.as_view(), name="create_usuario"),
    path("Usuarios/update/<int:usuario_id>/", views.UsuarioRetrieveUpdateAPIView.as_view(), name="update_usuario"),
    path("Usuarios/delete/<int:usuario_id>/", views.UsuarioDestroyAPIView.as_view(), name="delete_usuario"),

    # Rutas para Operadores
    path("Operadores/", views.OperadorListAPIView.as_view(), name="lista_operador"),
    path("Operadores/<int:operador_id>/", views.OperadorRetrieveAPIView.as_view(), name="detail_operador"),
    path("Operadores/create/", views.OperadorCreateAPIView.as_view(), name="create_operador"),
    path("Operadores/update/<int:operador_id>/", views.OperadorRetrieveUpdateAPIView.as_view(), name="update_operador"),
    path("Operadores/delete/<int:operador_id>/", views.OperadorDestroyAPIView.as_view(), name="delete_operador"),

    # Rutas para Vehiculos
    path("Vehiculos/", views.VehiculoListAPIView.as_view(), name="lista_vehiculo"),
    path("Vehiculos/<int:vehiculo_id>/", views.VehiculoRetrieveAPIView.as_view(), name="detail_vehiculo"),
    path("Vehiculos/create/", views.VehiculoCreateAPIView.as_view(), name="create_vehiculo"),
    path("Vehiculos/update/<int:vehiculo_id>/", views.VehiculoRetrieveUpdateAPIView.as_view(), name="update_vehiculo"),
    path("Vehiculos/delete/<int:vehiculo_id>/", views.VehiculoDestroyAPIView.as_view(), name="delete_vehiculo"),

    # Rutas para Refacciones
    path("Refacciones/", views.RefaccionesListAPIView.as_view(), name="lista_refaccion"),
    path("Refacciones/<int:refaccion_id>/", views.RefaccionesRetrieveAPIView.as_view(), name="detail_refaccion"),
    path("Refacciones/create/", views.RefaccionesCreateAPIView.as_view(), name="create_refaccion"),
    path("Refacciones/update/<int:refaccion_id>/", views.RefaccionesRetrieveUpdateAPIView.as_view(), name="update_refaccion"),
    path("Refacciones/delete/<int:refaccion_id>/", views.RefaccionesDestroyAPIView.as_view(), name="delete_refaccion"),

    # Rutas para Movimientos
    path("Movimientos/", views.MovimientosListAPIView.as_view(), name="lista_movimiento"),
    path("Movimientos/<int:id_movimiento>/", views.MovimientosRetrieveAPIView.as_view(), name="detail_movimiento"),
    path("Movimientos/create/", views.MovimientosCreateAPIView.as_view(), name="create_movimiento"),
    path("Movimientos/update/<int:id_movimiento>/", views.MovimientosRetrieveUpdateAPIView.as_view(), name="update_movimiento"),
    path("Movimientos/delete/<int:id_movimiento>/", views.MovimientosDestroyAPIView.as_view(), name="delete_movimiento"),
]
