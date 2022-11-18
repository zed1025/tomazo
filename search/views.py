from django.shortcuts import render

# Create your views here.
# https://stackoverflow.com/questions/42359112/access-form-data-of-post-method-in-django
def search(request):
    search_data = None
    if request.method == 'POST':
        search_data = request.POST.get('search_str')
        if search_data == '':
            print('Bad Input!')
        print(search_data)

    context = {}
    context['sr'] = search_data
    context['search_res'] = ['Amit', 'Shivam', 'Rushi', 'Naman']
    return render(request, 'search.html', context=context)
    