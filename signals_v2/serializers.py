from rest_framework import serializers
from .models import Signal, SignalSet


class SignalSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignalSet
        fields = ('signals',)


class SignalSerializer(serializers.ModelSerializer):
    value = serializers.ListField(child=serializers.IntegerField(min_value=0, max_value=1))

    class Meta:
        model = Signal
        fields = '__all__'
