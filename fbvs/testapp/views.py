from django.shortcuts import render,redirect
from testapp.models import Emplooye
from testapp.forms import Employeefrom
def retrive_view(request):
    emp_list=Emplooye.objects.all()
    return render(request,'testapp/index.html',{'emp_list':emp_list})
def retrive_formview(request):
    form=Employeefrom()
    if request.method=='POST':
      form=Employeefrom(request.POST)
      if form.is_valid():
        form.save()
      return redirect('/list')  
    return render(request,'testapp/form.html',{'form':form})
def del_view(request,id):
   emplooye=Emplooye.objects.get(id=id)
   emplooye.delete()
   return redirect('/list')
def up_view(request,id):
   emplooye=Emplooye.objects.get(id=id)
   form=Employeefrom(instance=emplooye)
   if request.method=='POST':
     form=Employeefrom(request.POST)
   if form.is_valid():
    form.save()
    return redirect('/list')  
   return render(request,'testapp/upform.html',{'form':form})
# Create your views here.
