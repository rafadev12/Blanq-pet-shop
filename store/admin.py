from django.contrib import admin
from .models import Combo

@admin.register(Combo)
class ComboAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_usd', 'badge', 'is_active', 'order')
    list_editable = ('price_usd', 'is_active', 'order')
    search_fields = ('title',)