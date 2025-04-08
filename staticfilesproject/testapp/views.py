from django.shortcuts import render

# Create your views here.
def info_view(request):
    my_dict={'s1':'dajango','s2':'html',
             's3':'css','s4':'js'}
    return render(request,'testapp/index.html',my_dict)