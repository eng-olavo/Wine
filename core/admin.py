from django.contrib import admin
from . import models




#@admin.register(Vinho)
class VinhoAdmin(admin.ModelAdmin):
    list_display = ('nome','cor','uva','acucar', 'safra', 'nacionalidade','destaque','ativo')

admin.site.register(models.Vinho, VinhoAdmin)