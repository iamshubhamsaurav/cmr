# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Home')


def customer(request):
    return HttpResponse('Customer')


def products(request):
    return HttpResponse('Products')
