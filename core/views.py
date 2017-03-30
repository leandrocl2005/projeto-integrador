from django.shortcuts import render, get_object_or_404
from .models import Capim

def lista_capim(request):
	qs = Capim.objects.all().order_by('-data_update')
	context = {
		"lista_capim": qs,
	}
	return render(request, "lista_itens.html", context)

def item_capim(request, id):
	capim = get_object_or_404(Capim, id=id)
	context = {
		"capim": capim,
	}
	return render(request, "item_capim.html", context)
