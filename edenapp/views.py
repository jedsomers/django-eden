from django.shortcuts import render
from django.utils import timezone
from .models import Design, User

from rest_framework import permissions, viewsets
from edenapp.serializers import UserSerlializer, DesignSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerlializer
    permission_classes = [permissions.IsAuthenticated]

class DesignViewSet(viewsets.ModelViewSet):
    queryset = Design.objects.all()
    serializer_class = DesignSerializer
    permission_classes = [permissions.IsAuthenticated]

def design_list(request):
    designs = Design.objects.order_by('updated_date')
    return render(request, 'edenapp/design_list.html', {'designs': designs})
