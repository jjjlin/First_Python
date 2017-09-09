from django.shortcuts import render
from .models import Recipe
from django.http import JsonResponse
from django.core import serializers
# Create your views here.


def get_recipe_api(request):
	recipes = Recipe.objects.all()
	data = serializers.serialize('json', recipes)
	return JsonResponse({'date': data})




	