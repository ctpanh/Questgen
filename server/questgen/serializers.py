from rest_framework import serializers
from .models import QuestionModel

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = ('id', 'file', 'easy', 'medium', 'hard', 'quest_type')

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = ('id', 'text', 'easy', 'medium', 'hard', 'quest_type')