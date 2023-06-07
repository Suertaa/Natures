from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import authenticate
from .forms import *
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
# Create your views here.
def home(request):
    prodCategory = Food.objects.all().order_by("-food_id")
    categories = Category.objects.all().order_by("-category_id")
    prodAdoption = Adopt.objects.all().order_by("-adopt_id")
    kategorit = Kategoria.objects.all().order_by("-kategoria_id")
    context = {"prodCategory":prodCategory,"categories" :categories ,"prodAdoption": prodAdoption ,"kategorit":kategorit}

    if request.method == 'POST':
        name_ = request.POST.get('name_', '')
        email = request.POST.get('email', '')

        if email:
            if Subscriber.objects.filter(email=email).exists():
                messages.warning(request, 'Email is already registered.')  # Display a warning message
            else:
                subscriber = Subscriber(name=name_, email=email)
                subscriber.save()
                messages.success(request, 'You have been successfully registered.')  # Display a success message
        else:
            messages.warning(request, 'Invalid email.')  # Display a warning message for invalid email
    
    return render(request, 'home.html',context)


def about(request):
    categories = Category.objects.all().order_by("-category_id")
    kategorit = Kategoria.objects.all().order_by("-kategoria_id")
    context = {"categories" :categories , "kategorit":kategorit}
    return render(request, 'about.html',context)

def adoption(request,id):
    categories = Category.objects.all().order_by("-category_id")
    kategorit = Kategoria.objects.all().order_by("-kategoria_id")
    detAdoption =  Kategoria.objects.get(kategoria_id=id)
    prodAdoption = Adopt.objects.filter(adopt_category=detAdoption).order_by("-adopt_id")
    context = {"detAdoption":detAdoption, "kategorit":kategorit, "prodAdoption":prodAdoption,"categories":categories}
    return render(request, 'adoption.html',context)

def category_products(request,id):
    categories = Category.objects.all().order_by("-category_id")
    kategorit = Kategoria.objects.all().order_by("-kategoria_id")
    detCategory = Category.objects.get(category_id=id)
    prodCategory = Food.objects.filter(food_category=detCategory).order_by("-food_id")
    context = {"detCategory":detCategory, "categories":categories, "prodCategory":prodCategory,"kategorit":kategorit}
    return render(request, 'category_products.html', context)


def contact(request):
    categories = Category.objects.all().order_by("-category_id")
    kategorit = Kategoria.objects.all().order_by("-kategoria_id")
    context = {"categories" :categories , "kategorit":kategorit}
    if request.method == "POST":
        emri = request.POST['name']
        email = request.POST['email']
        mesazhi = request.POST['mesazhi']
       
        Contact(contact_emri=emri,contact_email=email,contact_comment=mesazhi).save()
        messages.success(request,'Your message was sent.')

    return render(request, 'contact.html',context)
    

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    context = {'form':form}
    return render(request,'users/register.html', context)


def login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
    form = LoginForm()
    context = {'form':form}
    return render(request, 'users/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('/')