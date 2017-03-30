#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse

class Capim(models.Model):

    def upload_dir(instance, filename):
        return 'fotos-capim/%s' %(filename)

    nome_popular    = models.CharField("Nome popular", max_length = 120)
    nome_cientifico = models.CharField("Nome cientifíco", max_length = 120)
    descricao       = models.TextField("Descrição")
    fonte           = models.CharField("Fonte", max_length = 120)
    responsavel     = models.CharField("Responsável", max_length = 120)
    imagem          = models.ImageField("Imagem", upload_to = upload_dir, null = True, blank = True)
    data_criacao    = models.DateTimeField("Data da criação", auto_now = False, auto_now_add = True)
    data_update     = models.DateTimeField("Atualização", auto_now = True, auto_now_add = False)

    def __str__(self):
        return self.nome_popular

    def __unicode__(self):
        return self.nome_popular

    def get_url(self):
        return reverse("core:item_capim", kwargs={"id":self.id})
