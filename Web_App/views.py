from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from SportsNet import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token
from django.contrib import messages
from .models import *

import requests
API_KEY = '0e55381042014509ade53f0065695efc'

# Create your views here.

def home(request):
    url = f'https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']


    context = {
        'articles' : articles
    }
    return render(request, 'Web_App/index.html', context)

def sports(request):
    return render(request, 'Web_App/sports.html')

def organise(request):
    return render(request, 'Web_App/organise.html')

def event(request):
    events = Event.objects.all()
    context = {'events':events}
    return render(request, 'Web_App/event.html', context)
    
def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'Web_App/store.html', context)

def storef(request):
    if request.method == "POST":
        name = request.POST.get('name')
        pname = request.POST.get('pname')
        img = request.POST.get('img')
        local = request.POST.get('local')
        desc = request.POST.get('desc')
        storef = Storef(name=name, pname=pname, img=img, local=local, desc=desc, ) 

        storef.save()
        messages.success(request, 'Your form has been submitted!')
   
    return render(request, 'Web_App/storef.html')

def eventform(request):
     if request.method == "POST":
        name = request.POST.get('name')
        date = request.POST.get('date')
        email = request.POST.get('email')
        number = request.POST.get('number')
        local = request.POST.get('local')
        eventform = Eventform(name=name, date=date, email=email, number=number, local=local, ) 

        eventform.save()
        messages.success(request, 'Your form has been submitted!')

     return render(request, 'Web_App/eventform.html')


def organizer(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        img = request.POST.get('img')
        sport = request.POST.get('sport')
        email = request.POST.get('email')
        phonenumber = request.POST.get('number')
        address = request.POST.get('address')
        code = request.POST.get('code')
        organizer = Organizer(firstname=firstname, img=img, sport=sport, email=email,  phonenumber=phonenumber,  address=address,  code=code, ) 
        organizer.save()
        
        messages.success(request, 'Your form has been submitted!')      

    return render(request, 'Web_App/organizer.html')



def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signup')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('signup')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('signup')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('signup')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        # myuser.is_active = False
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        
        # Welcome Email
        subject = "Welcome to SportsNet Login!!"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to SportsNet!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\n SportsNet Team"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email @ SportsNet Login!!"
        message2 = render_to_string('email_confirmation.html',{
            
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [myuser.email],
        )
        email.fail_silently = True
        email.send()
        
        return redirect('signin')
        
        
    return render(request, "Web_App/signup.html")



def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('signin')
    else:
        return render(request,'activation_failed.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "Web_App/index.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('signin')
    
    return render(request, "Web_App/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('signin') 