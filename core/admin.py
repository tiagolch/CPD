from django.contrib import admin
from .models import *


@admin.register(Tonners)
class TonnersAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'quantidade', 'get_ultimaAlteracao']


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['empresa']


@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):
    list_display = ['setor']


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['categoria']


@admin.register(Abertura)
class AberturaAdmin(admin.ModelAdmin):
    list_display = ['id','status','empresa','setor', 'usuario','tecnico','categoria','get_dataAbertura','get_dataUltimaAlteracao','get_dataFechamento']
    list_display_links = ['id', 'status', 'usuario']
    list_filter = ['setor', 'categoria', 'status']
    list_max_show_all = 10
    list_per_page = 10
    search_fields = ['setor', 'usuario','tecnico', 'categoria', 'get_dataAbertura']
