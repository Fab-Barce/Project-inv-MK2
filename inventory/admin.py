from django.contrib import admin
from .models import Categoria
from .models import Empresa
from .models import Proveedor
from .models import Usuario
from .models import Operador
from .models import Vehiculo
from .models import Refacciones
from .models import Movimientos

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Empresa)
admin.site.register(Proveedor)
admin.site.register(Usuario)
admin.site.register(Operador)
admin.site.register(Vehiculo)
admin.site.register(Refacciones)
admin.site.register(Movimientos)
