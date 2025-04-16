from django.shortcuts import render
from testapp.models import Students
def student_view(request):
    student_list=Students.objects.all()
    my_dict={'students_list':student_list}
    return render(request,'testapp/index.html',my_dict)
# Create your views here.
