from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from taxi.utils import get_db_handle, get_collection_handle


DATABASE_NAME = 'tspds'
DATABASE_HOST = 'localhost'
DATABASE_PORT = '27017'
db_handle, mongo_client = get_db_handle(DATABASE_NAME, DATABASE_HOST, DATABASE_PORT)
collection = db_handle['register']

# Create your views here.
def home(request):
    return render(request,'index.html')

def signupform(request):
    return render(request,'signup.html')

def loginform(request):
    return render(request,'login.html')

def reset(request):
    return render(request,'resetpassword.html')

def signup(request):
    name = request.GET['username']
    email = request.GET['email']
    password = request.GET['password']
    s=set()
    cursor = collection.find({},{"email": 1})
    for i in cursor:
        s.add(i['email'])
    if email in s:
        return render(request,'signup.html',{'message': 'Email Id already exist'})
    else:
        dic = {'name':name,
               'email':email,
               'password':password}
        collection.insert_one(dic)
        return render(request,'login.html',{'message': 'Successfully Registered '+str(name)})
    
def login(request):
    email = request.GET['email']
    password = request.GET['password']
    dic = {}
    cursor = collection.find({},{"email": 1,"password":1})
    for i in cursor:
        dic[i['email']] = i['password']
    if email in dic.keys() and password in dic.values():
        return render(request,'product.html')
    elif email in dic.keys() and password not in dic.values():
        return render(request,'login.html',{'message': 'Incorrect Password'})
    else:
        return render(request,'login.html',{'message': 'Incorrect Email and Password'})
    


    

