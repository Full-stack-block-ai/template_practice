from django.shortcuts import render

# Create your views here.
def example_view(request):
    return render(request, 'my_app/example.html')

def variable_view(request):
    my_var = {'first_name': 'tim', 'last_name': 'minchin',
    'some_list':[1,2,3], 'some_dict':{'inside_key':'inside_value'},
    'list_with_spaces': 'This String Had Spaces Before The Cut Filter'}

    return render(request,'my_app/variable.html', context=my_var)