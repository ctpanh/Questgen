from rest_framework import serializers
from .models import FileModel

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = ('id', 'file', 'easy', 'medium', 'hard')

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = ('id', 'text', 'easy', 'medium', 'hard')