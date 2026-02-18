from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def receipe_page(request):
    queryset=Receipe.objects.all()

    if request.method=="POST":
        data=request.POST
        receipe_name=(data.get('receipe_name') or '').strip()
        receipe_description=(data.get('receipe_description') or '').strip()
        errors={}

        if len(receipe_name)==0:
            errors['receipe_name']='Receipe name cannot be empty.'
        if len(receipe_description)==0:
            errors['receipe_description']='Receipe description cannot be empty.'

        if errors:
            context={
                'receipes':queryset,
                'errors':errors,
                'form_data':{
                    'receipe_name':receipe_name,
                    'receipe_description':receipe_description,
                }
            }
            return render(request,'receipe.html',context)

        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description)
        return redirect('/')

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
        receipe_name=(data.get('receipe_name') or '').strip()
        receipe_description=(data.get('receipe_description') or '').strip()
        errors={}

        if len(receipe_name)==0:
            errors['receipe_name']='Receipe name cannot be empty.'
        if len(receipe_description)==0:
            errors['receipe_description']='Receipe description cannot be empty.'

        if errors:
            context['errors']=errors
            context['form_data']={
                'receipe_name':receipe_name,
                'receipe_description':receipe_description,
            }
            return render(request,'update_receipe.html',context)

        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description
        
        queryset.save()
        return redirect('/')
    return render(request,'update_receipe.html',context)



