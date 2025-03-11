from django.shortcuts import render
from .models import Product

def items_list(request):
    """Displays the items list page."""
    items = Product.objects.all()
    return render(request, 'items_list.html', {"items": items})


def items_details(request, item_id):
    """Displays the corresponding details per item."""
    item = Product.objects.filter(id=item_id).first()
    return render(request, 'items_details.html', {"item": item})

def home_page(request):
    """Displays the homepage with links to each app."""
    return render(request, 'home_page.html')
