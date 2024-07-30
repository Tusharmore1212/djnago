from django.shortcuts import render, redirect
from myapp.models import Service

# Create your views here.
def calculator(request):
    return render(request, 'index.html')

def even_odd(request):
    return render(request, 'even_odd.html')

def Result(request):
    num = request.GET.get('num')
    return render(request, 'result.html', {'num': num})

def showData(request):
    servicesData = Service.objects.all()
    print(servicesData)
    for a in servicesData:
        print(a.service_icon)
    data={
        'servicesData': servicesData
    }
    return render(request,'File_data.html',data)

def even_odd_result(request):
    ans = request.GET['ans']
    return render(request,'even_odd_result.html',{'ans':ans})
def checker(request):
    ans=""
    try:
        n1 = int(request.POST['n1'])
        if n1%2==0:
            ans = "EVEN"
        else:
            ans = "ODD"
    except:
        pass
    
    url = f"/even_odd_result/?ans={ans}"
    return redirect(url)

def calculate(request):
    try:
        n1 = float(request.POST['n1'])
        n2 = float(request.POST['n2'])
        operation = request.POST['operation']
        
        if operation == 'add':
            num = n1 + n2
        elif operation == 'subtract':
            num = n1 - n2
        elif operation == 'multiply':
            num = n1 * n2
        else:
            num = 'Invalid operation'

        url = f"/result/?num={num}"
        return redirect(url)
    except Exception as e:
        return render(request, 'index.html', {'error': str(e)})
