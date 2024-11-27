from django.shortcuts import render

# Create your views here.

def index(request):
    context={"name":"Binod","age":23}
    return render(request,'firstapp/index.html',context=context)
