from rest_framework import serializers
from .models import Snack


class SnackSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'description', 'created_at',)
        model = Snack
