from rest_framework import serializers

from .models import Category, Question


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields= ("id", "name")


class QuestionSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only = True, many = False)
    class Meta:
        model= Question
        fields= ("id", "title", "options", "correct_option", "category")

