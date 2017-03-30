from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^lista$', lista_capim, name="lista_capim"),
    url(r'^capim/(?P<id>\d+)$', item_capim, name="item_capim"),
]