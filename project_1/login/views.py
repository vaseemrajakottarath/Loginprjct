from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.sessions.models import Session
from .models import list1,card1
from django.views.decorators.cache import never_cache

# Create your views here.
dic={'list1':list1,'card1':card1}

@never_cache
def signin(request):
    if request.session.has_key('key'):
        return redirect('log')
    else:
        if request.method=='POST':
                username = request.POST['username']
                password = request.POST['password']
                if username=='vaseem' and password=='9900':
                    request.session['key']= 'True'
                    return redirect('log')
                else:
                    messages.info(request,'Invalid Username or password')
                    return redirect('signin')
        else:
            return render(request,'index.html')

@never_cache
def log(request):
   
    if request.session.has_key('key'):
        return render(request,'home.html',dic)
    else:
        return redirect('signin')
@never_cache
def logout(request):
     if request.session.has_key('key'):
        request.session.flush()

        return redirect('signin')