from rest_framework import serializers
from .models import ImagesModel
from django.core.validators import ValidationError


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesModel
        fields = ('id', 'name', 'url', 'picture', "width", 'height', 'parent_picture')


class ImageResizeSerializer(ImageSerializer):
    def validate(self, data):
        return super().validate(data)
