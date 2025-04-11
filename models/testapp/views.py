from django.shortcuts import render
from testapp.models import employess
def emp_data_views(request):
    my_list=employess.objects.all()
    my_dict={'my_list':my_list}
    return render(request,'testapp/index.html',my_dict)
# Create your views here.
