from rest_framework import serializers
from src.exchange.models import Exchange
from src.rate.models import Rate


class ExchangeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    rate = serializers.PrimaryKeyRelatedField(queryset=Rate.objects.all(), error_messages={
        'does_not_exist': 'Invalid ID "{pk_value}" - Rate does not exist.'})
    date = serializers.DateTimeField(required=False)
    value = serializers.FloatField(min_value=0)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Exchange.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.rate = validated_data.get('rate', instance.rate)
        instance.date = validated_data.get('date', instance.date)
        instance.value = validated_data.get('value', instance.value)
        instance.save()
        return instance