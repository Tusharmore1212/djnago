from django.shortcuts import render, redirect
from storedata.models import Store
from django.core.mail import send_mail
import re
from django.contrib.auth.hashers import make_password,check_password
from storedata.form import UserForms
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request, 'index.html')

def savedata(request):
    if request.method == "POST":
        fname = request.POST['firstName']
        lname = request.POST['lastName']
        email = request.POST['email']
        pswd = request.POST['password']
        cpswd = request.POST['confirmPassword']
        if not is_valid_password(pswd):
           error_message = "Enter valid password"
           print(error_message)
           return render(request, 'index.html', {'error_message': error_message})
        
        if pswd == cpswd:
            try:
                hashed_password = make_password(pswd)
                store = Store(fname=fname, lname=lname, email=email, password=hashed_password, cpassword=hashed_password)
                store.save()
                send_mail(
                    'Testing Mail',
                    'Registration sucessfull',
                    'tusharumore0285@gmail.com',
                    [email],
                    fail_silently=False,
                )
                return redirect('/login/')
            except :
            
                error_message = "Email already exists. Please use a different email."
                print(error_message)
                return render(request, 'index.html', {'error_message': error_message})
        else:
            return render(request, 'index.html', {'error': 'Passwords do not match'})

    return redirect('/')
# @login_required(login_url='login')
def displaydata(request):
    storeddata = Store.objects.all().order_by('fname')
    for i in storeddata:
        
        print(i.fname)
    context = {
        "storeddata": storeddata
    }
    return render(request, 'display.html', context)

def login_page(request):
    fn = UserForms()
    data ={
        'fn' : fn
    }
    if request.method == "POST":
        email = request.POST['email']
        pswd = request.POST['password']
        print(email,"ll")
        try:
            storeddata1 = Store.objects.get(email=email)
            if check_password(pswd, storeddata1.password):
                send_mail(
                    'Testing Mail',
                    'Login Sucessfull',
                    'tusharumore0285@gmail.com',
                    [email],
                    fail_silently=False,
                )
                return redirect('/displaydata/')  
            else:
                return render(request, 'Login.html', {'error': 'Invalid Credentials'})
        except Store.DoesNotExist:
            return render(request, 'Login.html', {'error': 'Invalid Credentials'})
    return render(request,'Login.html',data)

def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[a-zA-Z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    return True