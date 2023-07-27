from django.shortcuts import render,HttpResponse,redirect
from .models import Recipe
from django.db.models import Q

# Create your views here.
def recipes(request):
    if request.method == "POST":
        recipes_name = request.POST.get("recipe_name")
        recipes_description = request.POST.get("recipe_description")
        recipes_image=request.FILES.get("recipe_image")
        
        Recipe.objects.create(recipe_name=recipes_name,recipe_description=recipes_description,recipe_image=recipes_image)

        return redirect("recipes")
    
    return render(request,'recipes.html')

def recipe_info(request):
    if request.GET.get("search"):
        srch = request.GET.get("search")
        srch_info = Recipe.objects.filter(Q(recipe_name__icontains = srch) | Q(recipe_description__icontains = srch)).values()
        return render(request,'recipe_info.html',context={"recp":srch_info})

    recp_query = Recipe.objects.all().values()
    return render(request,'recipe_info.html',context={"recp":recp_query})

def del_recipe(request,pk):
    recipe_del = Recipe.objects.get(id=pk)
    recipe_del.delete()
    return redirect('recipe_info')

def update_recipe(request,pk):
    updt_id = Recipe.objects.get(id=pk)
    if request.method=="POST":
        recipes_name = request.POST.get("recipe_name")
        recipes_description = request.POST.get("recipe_description")
        recipes_image=request.FILES.get("recipe_image")

        updt_id.recipe_name = recipes_name
        updt_id.recipe_description = recipes_description

        if recipes_image:
            updt_id.recipe_image = recipes_image
        
        updt_id.save()
        return redirect("recipe_info")

    return render(request,'update.html',context={"updt":updt_id})