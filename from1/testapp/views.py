from django.shortcuts import render
from testapp.form import StudentForm
def student_input_view(request):
    submitted=False
    sname=''
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            print("form valudtaion sucees full")
            print("marks:",form.cleaned_data['marks'])
            print("name",form.cleaned_data['name'])
            print("email",form.cleaned_data["email"])
            print("feddback",form.cleaned_data["feed_back"])
            sname=form.cleaned_data['name']
            submitted=True
    else:
        form=StudentForm()
    my_dict={'form':form,'sname':sname}
    return render(
        request,'testapp/index.html',context=my_dict,)
# Create your views here.
