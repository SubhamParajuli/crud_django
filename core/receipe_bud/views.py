from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def receipe_page(request):
    if request.method=="POST":
        data=request.POST
        receipe_image=request.FILES.get('receipe_image')
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')

        Receipe.objects.create(
            receipe_image=receipe_image,
            receipe_name=receipe_name,
            receipe_description=receipe_description)
        return redirect('/')
    
    queryset=Receipe.objects.all()
    context={
        'receipes':queryset
    }   

    return render(request,'receipe.html',context)


def delete_receipe(request,id):
    receipe=Receipe.objects.get(id=id)
    receipe.delete()
    return redirect('/')


def update_receipe(request,id):
    queryset=Receipe.objects.get(id=id)
    context={
        'receipe':queryset
        }
    
    if request.method=="POST":
        data=request.POST
        receipe_image=request.FILES.get('receipe_image')
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')

        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description

        if receipe_image:
            queryset.receipe_image=receipe_image
        
        queryset.save()
        return redirect('/')
    return render(request,'update_receipe.html',context)



