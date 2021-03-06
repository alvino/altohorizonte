from django.contrib import admin

from .models import (
        Secretaria, 
        Assinatura, 
        CentroCusto, 
        Requerimento, 
        ItemRequerido,
        assinante,
        Unidade,
    )


class AssinaturaInline(admin.TabularInline):
    model = Assinatura
    extra = 1


class ItemRequeridoInline(admin.TabularInline):
    model = ItemRequerido
    extra = 1

class RequerimentoAdmin(admin.ModelAdmin):
    inlines = [
        ItemRequeridoInline,
        AssinaturaInline,
    ]


admin.site.register(Secretaria)
admin.site.register(assinante)
admin.site.register(CentroCusto)
admin.site.register(Unidade)
admin.site.register(Requerimento, RequerimentoAdmin)

