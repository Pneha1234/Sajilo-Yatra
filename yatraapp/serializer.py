from rest_framework import serializers

from .models import *


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('location', 'event_name', 'description','created_by')
