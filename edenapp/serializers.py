from django.contrib.auth.models import User, Design
from rest_framework import serializers

class UserSerlializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'designs')

class DesignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Design
        fields = ('url', 'title', 'description', 'creator')