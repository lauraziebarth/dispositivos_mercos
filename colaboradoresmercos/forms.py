# coding: utf-8
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from django import forms


class FormColaborador(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    area = forms.CharField(max_length=20)


class FormLogin(forms.Form):
    email = forms.CharField(max_length=100)

