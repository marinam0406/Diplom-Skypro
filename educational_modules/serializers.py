from rest_framework import serializers

from .models import EduModel


class EduSerializer(serializers.ModelSerializer):
    '''
    Serializer for EduModel model.
    '''
    class Meta:
        model = EduModel
        fields = ['number', 'name', 'description']
