from django.shortcuts import render

# Create your views here.
def my_info(request):
    return render(request,'tsetapp/index.html')
def my_movies(request):
    heder='my movies'
    sub_1='mad2 goog movie'
    sub_2='og comming soon but not conform date'
    sub_3='peddi march27'
    my_dict={'type':'movies','heder':heder,'sub_1':sub_1,'sub_2':sub_2,'sub_3':sub_3}
    return render(request,'tsetapp/news.html',my_dict)
def my_pot(request):
    heder="politics"
    sub_1='ap cm chandarababu nadiu'
    sub_2='app deputy cm pavan kalayan'
    sub_3='india pm naredra modi'
    my_dict={'type':'politics','heder':heder,'sub_1':sub_1,'sub_2':sub_2,'sub_3':sub_3}
    return render(request,'tsetapp/news.html',my_dict)
def my_sport(request):
    heder="politics"
    sub_1='punjab vs csk punjab won the match by 19 runs'
    sub_2='kkr vs lsg'
    sub_3='csk vs dc'
    my_dict={'type':'sport','heder':heder,'sub_1':sub_1,'sub_2':sub_2,'sub_3':sub_3}
    return render(request,'tsetapp/news.html',my_dict)
