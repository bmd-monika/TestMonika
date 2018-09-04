from rest_framework import serializers
from src.rate.models import Rate


class RateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fromRate = serializers.CharField(required=False, allow_blank=True, max_length=100)
    toRate = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Rate.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.fromRate = validated_data.get('fromRate', instance.title)
        instance.toRate = validated_data.get('toRate', instance.code)
        instance.save()
        return instance