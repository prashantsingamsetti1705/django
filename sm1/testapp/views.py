from django.shortcuts import render
def home_view(request):
    return render(request,'testapp/index.html')
# Create your views here.
def age_view(request):
    print(request.COOKIES)
    name=request.GET['name']
    response=render(request,'testapp/age.html',{'name':name})
    response.set_cookie('name',name)
    return response
def gf_view(request):
    print(request.COOKIES)
    name=request.COOKIES.get('name')
    age=request.GET.get('age')
    response=render(request,'testapp/gf.html',{'name':name,'age':age})
    response.set_cookie('age',age)
    return response
def reults_view(request):
    print(request.COOKIES)
    name=request.COOKIES.get('name')
    age=request.COOKIES.get('age')
    gf=request.GET.get('gf')
    return render(request,'testapp/results.html',{'name':name,'age':age,'gf':gf}) 