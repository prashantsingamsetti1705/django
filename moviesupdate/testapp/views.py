from django.shortcuts import render

def movie_update(request):
    return render(request,'testapp/index.html')
from testapp.models import Student
def movielist(request):
    movielist=Student.objects.all()
    return render(request,'testapp/movielist.html',{'movielist':movielist})
# Create your views here.
from testapp.forms import StudentForm
def add_movie(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('Record inserted into DB successfully.....')
    form = StudentForm()
    return render(request,'testapp/addmovie.html',{'form':form})


