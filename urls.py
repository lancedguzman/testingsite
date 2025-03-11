from django.urls import path
from . views import items_list, items_details, home_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('merchstore/items/', items_list, name='items_list'),
    path('merchstore/item/<int:item_id>', items_details, name='items_details'),
]