from django.shortcuts import render ,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from testapp.froms import SingupForm
def home_view(request):
    return render(request,'testapp/home.html')
def logout_view(request):
    return render(request,'testapp/logout.html')
@login_required
def java_view(request):
    return render(request,'testapp/java.html')
@login_required
def python_view(request):
    return render(request,'testapp/python.html')
@login_required
def appi_view(request):
    return render(request,'testapp/appi.html')
def singup(request):
    if request.method == 'POST':
        form = SingupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
    else:
        form = SingupForm()

    return render(request, 'testapp/singup.html', {'form': form})
# Create your views here.
