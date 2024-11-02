from datetime import datetime
from urllib import request
from django.shortcuts import get_object_or_404, redirect, render
from .models import client
from .models import Project
from .models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.http import JsonResponse
from django.views import View
from django.utils import timezone
import json


# Create your views here.
def home(request):
    return render(request, 'home.html')

# def main_page(request):
#     return render(request, 'main.html')

def users_page(request):
    return render(request, 'user.html')

def clients_page(request):
    return render(request, 'clients.html')

def projects_page(request):
    return render(request, 'projects.html')

def get_all_clients(request):
    list1=client.objects.all()
    return render(request,'allclients.html',{'li':list1})

def create_new_client(request):
    if request.method == 'POST':
        id=request.POST['clid']
        client_name=request.POST['clname']
        created_at=request.POST['clcrat']
        created_by=request.POST['clcrby']
        client1 = client(id=id, client_name=client_name, created_at=created_at, created_by=created_by)
        client1.save()
        print('Client Added')
        return redirect('/')
    else:
         return render(request,'createclient.html')

def update_client(request):
    if request.method == 'POST':
        tempid = request.POST.get('client_id')
        new_name = request.POST.get('new_name')
        try:
            client1 = client.objects.get(id=tempid)
            client1.client_name = new_name
            client1.save()
            #messages.success(request, 'Client details updated successfully.')
            return redirect('/')
        except client.DoesNotExist:
            messages.error(request, 'Client not found.')
    
    return render(request, 'updateclient.html')

def get_clientby_id(request):
    if request.method == 'POST':
        tempid = request.POST.get('client_id')
        try:
            temp1 = client.objects.get(id=tempid)
            return render(request,'clientbyidans.html',{'item':temp1})
        except client.DoesNotExist:
            messages.error(request, 'Client not found.')
    return render(request, 'clientbyid.html')

def delete_client(request):
    if request.method == 'POST':
        tempid = request.POST.get('client_id')
        try:
            client1 = client.objects.get(id=tempid)
            client1.delete()
            return HttpResponse(status=204)
            #return redirect('/')
        except client.DoesNotExist:
            messages.error(request, 'Client not found.')

    return render(request, 'deleteclient.html')

# #Project------

def get_all_projects(request):
    prolist=Project.objects.all()
    return render(request,'allprojects.html',{'prolist':prolist})


def create_new_project(request):
    if request.method == 'POST':
        id=request.POST['plid']
        project_name=request.POST['plname']
        created_at=request.POST['plcrat']
        created_by=request.POST['plcrby']
        client_id=request.POST['clid']
        #Create object
        Project1 = Project(id=id, project_name=project_name, created_at=created_at, created_by=created_by, client_id=client_id)
        Project1.save()
        print('Project Added')
        return redirect('/')
    else:
        return render(request,'createproject.html')
    

#User
def create_new_user(request):
    if request.method == 'POST':
        id=request.POST['uid']
        user_name=request.POST['uname']
        name=request.POST['name']
        email=request.POST['email']
        contact=request.POST['con']
        
        user1 = User(id=id, user_name=user_name, name=name, email=email, contact=contact)
        user1.save()
        print('User Added')
        return redirect('/')
    else:
        return render(request,'createuser.html')
    

def get_all_user(request):
    userlist=User.objects.all()
    return render(request,'allusers.html',{'userlist':userlist})
