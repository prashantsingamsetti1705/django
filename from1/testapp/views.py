from django.shortcuts import render
from testapp.form import StudentFrom
def student_input_view(request):
    submitted=False
    sname=''
    if request.method=='POST':
        form=StudentFrom(request.POST)
        if form.is_valid():
            print("form valudtaion sucees full")
            print("marks:",form.cleaned_data['marks'])
            print("name",form.cleaned_data['name'])
            print("email",form.cleaned_data["email"])
            print("feddback",form.cleaned_data["feed_back"])
        sname=form.cleaned_data['name']
        submitted=True
    form=StudentFrom()
    my_dict={'form':form,'submitted':submitted,'sname':sname}
    return render(
        request,'testapp/index.html',context=my_dict,)
# Create your views here.
