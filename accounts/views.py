# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def home(request):
    # return HttpResponse('Home')
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()

    pending = orders.filter(status="Pending").count()
    delivered = orders.filter(status="Delivered").count()

    context = {'orders': orders, 'customers': customers, 'total_customers': total_customers,
               'total_orders': total_orders, 'pending': pending, 'delivered': delivered}
    return render(request, 'accounts/dashboard.htm', context)


def customers(request):
    customers = Customer.objects.all()
    return render(request, 'accounts/customers.htm', {'customers': customers})


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.htm', {'products': products})
