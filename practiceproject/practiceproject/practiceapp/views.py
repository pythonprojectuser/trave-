from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
#def home(request):
    #return HttpResponse("Heyy")
#def about(request):
    #return render(request,"about.html")
#def contact(request):
    #return HttpResponse("am contact")
#def detail(request):
   # return render(request,"details.html")
#def thanks(request):
    #return HttpResponse("ThankYou")

from . models import Place
from . models import Teams
def test(request):
     obj= Place.objects.all()
     obj2=Teams.objects.all()
     return render(request, 'index.html',{'result':obj,'result1':obj2,})


#def addition(request)
 #   x = int(request.GET['num1'])
  # res = x + y
   # res1 = x - y
    #res2 = x * y
    #res3 = x / y

    #return render(request, "result.html", {'result': res, 'result1': res1, 'result2': res2, 'result3': res3})