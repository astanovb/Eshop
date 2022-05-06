from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from simple_search import search_filter
# Create your views here.









def LogIN(request):
    pagge = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get('username')
        except:
            messages.error(request, 'User not registered yet')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(username, password)
            return redirect('index')

    return render(request, 'loginPage.html', {})




def LogOUT(request):
    logout(request),
    return redirect('index')


def index(request):
    carousel = Carousels.objects.all()
    products = Products.objects.all()
    categors = categories.objects.all()
    deliver = delivery.objects.all()
    about = About.objects.all()
    content = {'cars':carousel, 'del':deliver, 'prod':products, 'categores':categors, 'abut': about}
    return render(request, 'index.html', content)

def category(request, pk):
    categors = categories.objects.all()
    products = Products.objects.filter(cat=pk)
    content = {'prod':products, 'categores':categors}
    return render(request, 'categories.html', content)




def search_results(request):
    all_ids = []


    categors = categories.objects.all()

    if request.method == 'GET'  and request.GET.get('search') and request.GET.get != None:
        searchKeywords = request.GET.get('search').lower().split(' ') 
        
        for element in searchKeywords:
            search_fields = ['title', 'description']
            sf = search_filter(search_fields, element)
            f_products = Products.objects.filter(sf)


            for item in f_products:
                if not item.id in all_ids:
                    all_ids.append(item.id)

        result  = Products.objects.filter(id__in=all_ids)
        content = {'prod':result, 'categores':categors}
        return render(request, 'index.html', content)
    else :
        pass


def buypage(request, pk):
    categors = categories.objects.all()
    products = Products.objects.filter(id=pk)
    content = {'prod':products, 'categores':categors}
    return render(request, 'buypage.html', content)
