from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request,'index.html')
def about_us(request):
    return render(request,'about_us.html')
def contact(request):
    return render(request,'contact.html')
def Departments(request):
    return render(request,'Departments.html')
def Admission(request):
    return render(request,'Admission.html')
def Result(request):
    re  = request.GET.get('output')
    re2  = request.GET.get('output2')
    print(re)
    print(re2)
    return render(request,'thanks.html',{'output':re,'output2':re2})
def userForm(request):
    return render(request,'userForm.html')

def submitForm(request):
    data=None
    try:
        n1 = int(request.POST['field1'])
        print(n1)
        n2 = int(request.POST['field2'])
        data=n1+n2
        print(data)
        data2=22
        url="/result/?output={}&output2={}".format(data,data2)
        return HttpResponseRedirect(url)
    except:
        pass