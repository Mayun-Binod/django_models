from django.shortcuts import render
from firstapp.models import Employee
# Create your views here.

def index(request):
    emp_list=Employee.objects.all()
    context={"emp_list":emp_list}
    return render(request,'firstapp/index.html',context=context)

# def index(request):
#     emp_list=Employee.objects.all()
#     return render(request,'firstapp/index.html',{"emp_list":emp_list})
