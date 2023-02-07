# from django.http import JsonResponse
# from django.shortcuts import render
# from django.views import View

# from .models import Category, Question


# class QuestionsView (View):
#     def get (self, request ):
#         questionList = Question.objects.all()
#         return JsonResponse(list(questionList.values()),safe = False)

# class CategoriesView (View):
#     def get (self, request ):
#         categoryList = Category.objects.all()
#         return JsonResponse(list(categoryList.values()),safe = False)