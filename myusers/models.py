# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=150, db_index=True)
    last_name = models.CharField(max_length=150, db_index=True)
    number_of_login = models.IntegerField()

    class Meta:
        ordering = ('id',)
        index_together = (('id'),)
        db_table = "Users"


    def __str__(self):
        return self.last_name