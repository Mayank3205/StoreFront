from importlib import reload

from django.shortcuts import render
from django.db.models import Q, F
from store.models import Products, OrderItem, Order, Customer


# Create your views here.

# 44

def say_hello(request):
    # order_items = OrderItem.objects.values('product__id').distinct()
    # queryset = Products.objects.order_by('title').filter(id__in=order_items)


    # queryset = Products.objects.select_related('collection').all()

    # queryset = Products.objects. filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')

    queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[0:5]

    return render(request, 'hello.html', {'name':'Mayank',  'orders':list(queryset)})
