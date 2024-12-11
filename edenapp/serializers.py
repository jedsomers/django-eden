from django.contrib.auth.models import User
from .models import Design
from rest_framework import serializers

class UserSerlializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class DesignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Design
        fields = ('url', 'title', 'description', 'creator')