from django.shortcuts import render
from testapp.form import StudentFrom
def student_input_view(request):
    form=StudentFrom()
    my_dict={'form':form}
    return render(
        request,'testapp/index.html',context=my_dict)
# Create your views here.
