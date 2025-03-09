from django.shortcuts import render
from .models import Product

def items_list(request):
    items = Product.objects.all()
    return render(request, 'items_list.html', {"items": items})

def items_details(request, item_id):
    item = Product.objects.filter(id=item_id).first()
    return render(request, 'items_details.html', {"item": item})

