from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import login
from django.bootstrap import bootstrap
def index(request):
    return (request,'first_app/Home.html')
def login(request):
    user=login.objects.order_by('first_name')
    user2={"utilisateur":user}
    return render(request,'first_app/login.html',context=user2)
# Create your views here.
