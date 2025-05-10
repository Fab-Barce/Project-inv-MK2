from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from ..models import Refacciones
from django.conf import settings

# Lista de correos a notificar
LISTA_CORREOS = ["inventario@empresa.com", "fabian01enrique@gmail.com", "angel.oso.rafael@gmail.com" ]

@receiver(post_save, sender=Refacciones)
def verificar_stock_minimo(sender, instance, created, **kwargs):
    # Si fue eliminado, no hay forma de que post_save se dispare, así que no necesitas manejar eso aquí
    # Solo verificamos si la cantidad está por debajo del mínimo
    if instance.cantidad < instance.stock_minimo:
        asunto = f"⚠️ Stock bajo para {instance.nombre}"
        mensaje = (
            f"El producto '{instance.nombre}' tiene una cantidad actual de {instance.cantidad}, "
            f"por debajo del stock mínimo requerido de {instance.stock_minimo}.\n\n"
            f"Revisa el inventario lo antes posible."
        )
        try:
            send_mail(
                asunto,
                mensaje,
                settings.DEFAULT_FROM_EMAIL,
                LISTA_CORREOS,
                fail_silently=False,
            )
        except Exception as e:
            # Evita errores críticos si falla el envío de correo
            print(f"Error al enviar correo de stock bajo: {e}")
