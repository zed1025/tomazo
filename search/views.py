from django.shortcuts import render
from search.models import FoodItem, Restaurant

# Create your views here.
# https://stackoverflow.com/questions/42359112/access-form-data-of-post-method-in-django
def search(request):
    search_empty = False
    search_data = None
    if request.method == 'POST':
        search_data = request.POST.get('search_str')
        if search_data == '':
            search_empty = True
            print('Bad Input!')
        print(search_data)

    context = {}
    if search_empty:
        return render(request, 'search.html', context=context)
    context['sr'] = search_data
    search_terms = search_data.split()
    food_items = []
    restaurants = []
    for term in search_terms:
        # check if term is in any food title or description
        # get those food items
        data = FoodItem.objects.filter(name__icontains=term)
        print('data is of type: ', type(data))
        for x in data:
            # check if they are already in the array
            if x not in food_items:
                # if not add them
                food_items.append(x)
        data2 = FoodItem.objects.filter(description__icontains=term)
        for x in data2:
            if x not in food_items:
                food_items.append(x)

        # do the same for restaurants
        data3 = Restaurant.objects.filter(name__icontains=term)
        for x in data3:
            if x not in restaurants:
                restaurants.append(x)

    context['food_items'] = food_items
    context['restaurants'] = restaurants
    return render(request, 'search.html', context=context)
    