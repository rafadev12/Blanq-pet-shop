from django.shortcuts import render
from .models import Combo

def index(request):
    combos = Combo.objects.filter(is_active=True)
    return render(request, 'store/index.html', {'combos': combos})
