from django.shortcuts import render

# Create your views here.
def ifcondition(request):
    # d={'a':100}
    return render(request,'ifcondition.html',context={'a':200})