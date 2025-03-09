from django.urls import path
from . views import items_list, items_details

urlpatterns = [
    path('merchstore/items/', items_list, name='items_list'),
    path('merchstore/item/<int:item_id>', items_details, name='items_details'),
]