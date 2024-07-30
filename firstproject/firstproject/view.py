from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    data={
        "title":"home new",
        "Names" :["Tushar","avadut","ram"] ,
        "user_data":[
            {"name":"tushar","age":22},
            {"name":"ram","age":23}
        ],
        "Numbers":[10,20,30,40,50] 
    }

    return render(request,"index.html",data)
def aboutUs(request):
    return render(request,"aboutUs.html")
def career(request):
    return render(request,"career.html")
def products(request):
    return render(request,"Products.html")


