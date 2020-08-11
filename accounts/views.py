# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # return HttpResponse('Home')
    return render(request, 'accounts/dashboard.htm')


def customers(request):
    return render(request, 'accounts/customers.htm')


def products(request):
    return render(request, 'accounts/products.htm')
