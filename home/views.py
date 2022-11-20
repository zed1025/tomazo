from django.shortcuts import render
from search.models import FoodItem

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def new(request):
    all_foods = FoodItem.objects.all()
    context = {}
    context['all_foods'] = all_foods
    return render(request, 'new.html', context)

    