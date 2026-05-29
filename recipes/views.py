import re
from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, Favorite
from .forms import RecipeForm

def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    raw = recipe.ingredients
    items = raw.split(",")

    ingredients_list = [
        re.sub(r"^\d+\.\s*", "", item).strip()
        for item in items
        if item.strip()
    ]

    return render(request, "recipes/detail.html", {
        "recipe": recipe,
        "ingredients_list": ingredients_list
    })


def index(request):
    query = request.GET.get('q')

    if query:
        recipes = Recipe.objects.filter(title__icontains=query)
    else:
        recipes = Recipe.objects.all()

    return render(request, "recipes/index.html", {
        "recipes": recipes
    })


def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RecipeForm()

    return render(request, "recipes/create.html", {"form": form})