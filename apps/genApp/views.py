from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string
def index(request):
    counter=request.session.get('counter',0)
    request.session ['counter']= counter+1
    return render(request,'genApp/index.html') #You ALWAYS NEED A REQUEST!!

def randomGen(request):
    request.session ['random_word']= get_random_string(length=14) # rememeber its a dictionar NOT A LIST!!! so use {}!
    return redirect('/')

def reset(request):
    del request.session['random_word']
    request.session ['counter']=0
    return redirect('/')
# Create your views here.
