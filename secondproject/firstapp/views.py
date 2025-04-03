from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.
def time_info(reqsuest):
    date=datetime.datetime.now()
    msg='<h1>hello freind good evening</h1>'
    msg+='<h2>now time datetime'+str(date)+'</h2>'
    return HttpResponse(msg)