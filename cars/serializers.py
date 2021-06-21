from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import Car

class CarSerializer(ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'maker',
            'year',
            'admin',
        )

        model = Car