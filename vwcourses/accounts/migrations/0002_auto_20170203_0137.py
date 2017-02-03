# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 01:37
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='O nome de usuário é um campo obrigatório de até 30 caracteres ou menos, entre eles letras e números', max_length=30, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@-_]+$', 32), 'O nome de usuário só pode conter letras, números e simbolos como /@/./-/_', 'invalid')], verbose_name='Nome de Usuário'),
        ),
    ]
