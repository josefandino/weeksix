from rest_framework import serializers
from apps.tags.models import Tags


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'
