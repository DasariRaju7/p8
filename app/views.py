from django.shortcuts import render

# Create your views here.
def data(request):
    data='this data is mine'
    d={'assumption':data}
    
    return render(request,'data.html',context=d)
