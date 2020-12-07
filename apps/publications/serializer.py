from rest_framework import serializers
from apps.publications.models import Publications


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publications
        fields = '__all__'
