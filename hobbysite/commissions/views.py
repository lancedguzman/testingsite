from django.shortcuts import render
from .models import Commission

def commissions_list(request):
    commissions = Commission.objects.all()
    return render(request, 'commission_list.html', {'commissions': commissions})

def commission(request, id):
    commission = Commission.objects.get(id=id) 
    return render(request, 'commission.html', {'commission': commission})
