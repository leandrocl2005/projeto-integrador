from django.contrib import admin
from .models import Capim

@admin.register(Capim)
class CapimModelAdmin(admin.ModelAdmin):
	list_filter   = ("responsavel",)
	search_fields = ["nome_popular", "nome_cientifico", "descricao"]
	class Meta:
		model = Capim
