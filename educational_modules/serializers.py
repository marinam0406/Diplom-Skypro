from rest_framework import serializers

from .models import EduModel


class EduSerializer(serializers.ModelSerializer):
    class Meta:
        model = EduModel
        fields = ['number', 'name', 'description']
