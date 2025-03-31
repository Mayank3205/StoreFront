from importlib import reload

from django.db.models import Count
from django.db import transaction
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Products, Collection, Order, OrderItem
from tags.models import TaggedItem


# Create your views here.

# 44
def say_hello(request):




    return render(request, 'hello.html', {'name': 'Mayank', 'result': result})



    # with transaction.atomic():
    #     order = Order()
    #     order.customer_id = 1
    #     order.save()
    #
    #     item = OrderItem()
    #     item.order = order
    #     item.product_id = 1
    #     item.unit_price = 10
    #     item.quantity = 1
    #     item.save()


    # collections = Collection(pk=11)
    # collections.title = 'Games'
    # collections.featured_product = None
    # collections.save()

# from django.db.models import Q, F, Func, Value, ExpressionWrapper, DecimalField
# from django.db.models.aggregates import Sum, Count, Avg, Max, Min
# from store.models import Products, OrderItem, Order, Customer
# def say_hello(request):
#     # order_items = OrderItem.objects.values('product__id').distinct()
#     # queryset = Products.objects.select_related('collection').all()
#     # queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[0:5]
#     # queryset = Products.objects.values('title').filter(id__in = OrderItem.objects.values('product_id')).order_by('title').distinct()
#     # queryset = Order.objects.select_related('customer').filter(payment_status='P').order_by('-placed_at')[0:5]
#     # queryset = Products.objects.prefetch_related('promotions')
#     # result = Products.objects.aggregate(count=Count('id'), min_price=Min('unit_price'), max_price=Max('unit_price'))
#     # queryset = Order.objects.select_related('customer').order_by('-placed_at')[0:5]
#
#     # queryset = Customer.objects.annotate(
#     #     # concat
#     #     full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
#     # )
#     discounted_price =  ExpressionWrapper(F('unit_price') * 0.8,output_field=DecimalField())
#     queryset = Products.objects.annotate(
#         discounted_price=  discounted_price
#     )
#
#     return render(request, 'hello.html', {'name':'Mayank',  'order':list(queryset)})
