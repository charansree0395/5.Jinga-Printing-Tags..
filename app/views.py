from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse



def King(request):
    d={'name':'Anu','age':23,'class':12}
    return render(request,'print.html',d)