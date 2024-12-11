from django.shortcuts import render
from django.utils import timezone
from .models import Design

def design_list(request):
    designs = Design.objects.order_by('updated_date')
    return render(request, 'edenapp/design_list.html', {'designs': designs})
