from django.shortcuts import render
from testapp.models import StudentModel
def dept_view(request):
    record=StudentModel.objects.all()
    return render(request,'testapp/index.html',{'record':record})
# Create your views here.
