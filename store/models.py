from django.db import models

class Combo(models.Model):
    title = models.CharField(max_length=100, help_text="Ej: 2 Guantes/Packs")
    price_usd = models.DecimalField(max_digits=6, decimal_places=2, help_text="Precio en $")
    subtitle = models.CharField(max_length=150, default="Pet Glove Wipes")
    badge = models.CharField(max_length=50, blank=True, null=True, help_text="Ej: Más Popular")
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} - ${self.price_usd}"

    def whatsapp_link(self):
        text = f"¡Hola BLANQ! Quisiera ordenar la promo de {self.title} por ${int(self.price_usd)}."
        import urllib.parse
        return f"https://wa.me/584248183874?text={urllib.parse.quote(text)}"
