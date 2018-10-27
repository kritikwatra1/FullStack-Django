from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Webpage, AccessRecord, Topic

# Create your views here.
# def showmyapp(response):
#     return HttpResponse("<em>My Second App</em>")
# def index(request):
#     link = {'directme':'I am in views.py'}
#     return render(request,'parttwo\index.html',context = link)

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,'parttwo\index.html',context = date_dict)
