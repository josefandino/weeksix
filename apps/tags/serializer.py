from rest_framework import serializers
<<<<<<< HEAD
from apps.tags.models import Tag
=======
from .models import Tag
>>>>>>> 13ddd2046f9259766f16ab407bf620a236704a09


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
<<<<<<< HEAD
        fields = ['name']
=======
        fields = ['id', 'name']
>>>>>>> 13ddd2046f9259766f16ab407bf620a236704a09
