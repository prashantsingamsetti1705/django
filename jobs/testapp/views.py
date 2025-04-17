from django.shortcuts import render
from testapp.models import Hydinfo,Puneinfo,Banginfo
# Create your views here.
def home_page_view(request):
    return render(request,'testapp/index.html')
def hyd_page_view(request):
    hyd_list=Hydinfo.objects.all()
    mydict={'type':'hyd','hyd_list':hyd_list}
    return render(request,'testapp/news.html',mydict)
def pune_page_view(request):
    pune_list=Puneinfo.objects.all()
    mydict={'type':'pune','pune_list':pune_list}
    return render(request,'testapp/news.html',mydict)
def bang_page_view(request):
    bang_list=Hydinfo.objects.all()
    mydict={'type':'bang','bang_list':bang_list}
    return render(request,'testapp/news.html',mydict)
