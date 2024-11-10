
from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm
# Create your views here.

def user_list(request):
    records=User.objects.all()
    mydict={'records':records}
    return render(request,'Listingpage.html',context=mydict)

def AddUser(request):
    mydict={}
    form=UserForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('user_list')

    mydict['form']=form
    return render(request,'Add.html',mydict)

def EditUser(request,id=None):
    one_rec=User.objects.get(pk=id)
    form=UserForm(request.POST or None,request.FILES or None, instance=one_rec)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    mydict= {'form':form}
    return render(request,'Edit.html',context=mydict)

def DeleteUser(request,eid=None):
    one_rec = User.objects.get(pk=eid)
    if  request.method=="POST":
         one_rec.delete()
         return redirect('user_list')
    return render(request,'Delete.html')

def ViewUser(request,eid=None):
    mydict={}
    one_rec = User.objects.get(pk=eid)
    mydict['user']=one_rec
    return render(request,'''View.html''',mydict)