from django.shortcuts import render
from testapp.fomrs import StudentForm
def stu_view(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("record enterd sucessfully")
    form=StudentForm()
    return render(request,'testapp/index.html',{'form':form})
# Create your views here.
