from django.shortcuts import render
from testapp.forms import Name_form,Age_form,Gf_form
# Create your views here.
def home_view(request):
    form=Name_form()
    return render(request,'testapp/home.html',{'form':form})
def age_view(request):
    name=request.GET['name']
    request.session['name']=name
    form=Age_form()
    return render(request,'testapp/age.html',{'form':form,'name':name})
def gf_view(request):
    age=request.GET['age']
    request.session['age']=age
    name=request.session['name']
    form=Gf_form()
    return render(request,'testapp/gf.html',{'form':form,'name':name})
def res_view(request):
    gf=request.GET.get('gf')
    request.session['gf']=gf
    name=request.session['name']
    age=request.session['age']
    return render(request,'testapp/res.html')