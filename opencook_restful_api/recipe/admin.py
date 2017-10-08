from django.contrib import admin
from recipe.models import Recipe
from recipe.models import Test

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
	list_display = ('id', 'title')
		
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Test)
