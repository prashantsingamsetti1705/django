from django.shortcuts import render
def home_viwe(request):
    return render(request,'testapp/index.html')
# Create your views here.
from testapp.forms import Additems_from
def additem(request):
    form=Additems_from()
    response=render(request,'testapp/item.html',{'form':form})
    if request.method=="POST":
        form=Additems_from(request.POST)
        if form.is_valid():
            name=form.cleaned_data['itemname']
            quantity=form.cleaned_data['quantity']
            response.set_cookie(name,quantity)
    return response
def list_view(request):
    return render(request,'testapp/list.html')
