from ast import Name
from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from .models import *
import os
import random

# Create your views here.
def home(request):
    return render(request,"index.html")

def decrypt(request):
    try:
        if (request.method=="POST"):
            file=request.FILES.get('enfile')
            recieved=recieved_file()
            recieved.file=file
            temp=random.randint(2,7)
            recieved.key=temp
            recieved.save()
            id=recieved.id
            name=recieved.file.name

            connection=open("./media/"+name,"r")
            text=connection.read()
            connection.close()

            connection=open("./media/"+name,"w")
            
            newfile=""
            for i in text:
                newfile+=chr(ord(i)+temp)
            

            connection.write(newfile)
            connection.flush()
            connection.close()    
            download="/media/"+name
            
        return render(request,"index.html",{"key":temp,"Name":name[6:],"load":download})
    except:
        messages.error(request, "Please select any text file")

    return render(request,"index.html")

def enrypt(request):
    try:
        if (request.method=="POST"):
            file1=request.FILES.get('defile')
            Key=int(request.POST.get("key"))
            d=dfile()
            d.dtext=file1
            d.save()
            id=d.id
            name=d.dtext.name
            connection=open("./media/"+name,"r")
            text=connection.read()
            connection.close()

            connection=open("./media/"+name,"w")
            newfile=""
            for i in text:
                newfile+=chr(ord(i)-Key)
            

            connection.write(newfile)
            connection.flush()
            connection.close()
            download="/media/"+name
            
        return render(request,"index.html",{"Name1":name[10:],"load":download})
    except:
        messages.error(request, "Please select any text file")

    return render(request,"index.html")


