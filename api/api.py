
from rest_framework import permissions, viewsets

from .models import Category, Question
from .serializers import CategorySerializer, QuestionSerializer


class QuestionViewSet (viewsets.ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = QuestionSerializer

class CategoryViewSet (viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer