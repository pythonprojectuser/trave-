from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Carlist
from . form import CarlistForm

# Create your views here.
def demo(request):
    carlist=Carlist.objects.all()
    context={
        'car_list':carlist
    }

    return render(request,'index.html',context)
def details(request,car_id):
        carlist=Carlist.objects.get(id=car_id)
        return render(request,"detail.html",{'carlist':carlist})
def add_car(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        mnum=request.POST.get('mnum', )
        desc=request.POST.get('desc', )
        year=request.POST.get('year', )
        img=request.FILES['img']
        carlist=Carlist(name=name,desc=desc,year=year,mnum=mnum,img=img)
        carlist.save()
        return render(request, 'add.html')
def update(request,id):
    carlist=Carlist.objects.get(id=id)
    form=CarlistForm(request.POST or None,request.FILES,instance=carlist)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'carlist':carlist})
def delete(request,id):
    if request.method=="POST":
        carlist=Carlist.objects.get(id=id)
        carlist.delete()
        return redirect('/')
    return render(request,'delete.html')




