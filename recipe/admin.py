from django.contrib import admin
from .models import Category
from .models import Recipe
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    ...

# @admin.register(Recipe)  outra forma de registrar
class RecipeAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)