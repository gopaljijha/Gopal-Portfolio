from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from project import settings #geeksforgeeks to project
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from django.utils.encoding import force_bytes, force_text
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
# from . tokens import generate_token
from .forms import SignupForm
from .tokens import account_activation_token  


# Create your views here.


# def signup(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         email = request.POST['email']
#         pass1 = request.POST['pass1']
#         pass2 = request.POST['pass2']
        
#         if User.objects.filter(username=username):
#             messages.error(request, "Username already exist! Please try some other username.")
#             return redirect('signoutHome')
        
#         if User.objects.filter(email=email).exists():
#             messages.error(request, "Email Already Registered!!")
#             return redirect('signoutHome')
        
#         if len(username)>20:
#             messages.error(request, "Username must be under 20 charcters!!")
#             return redirect('signoutHome')
        
#         if pass1 != pass2:
#             messages.error(request, "Passwords didn't matched!!")
#             return redirect('signoutHome')
        
#         if not username.isalnum():
#             messages.error(request, "Username must be Alpha-Numeric!!")
#             return redirect('signoutHome')
        
#         myuser = User.objects.create_user(username, email, pass1)
#         myuser.first_name = fname
#         myuser.last_name = lname
#         # myuser.is_active = False
#         myuser.is_active = False
#         myuser.save()
#         messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        
#         # Welcome Email
#         subject = "Welcome to Gopalji-Creation"
#         message = "Hello " + myuser.first_name + "!! \n" + "Welcome to GFG!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address."        
#         from_email = settings.EMAIL_HOST_USER
#         to_list = [myuser.email]
#         send_mail(subject, message, from_email, to_list, fail_silently=True)
        
#         # Email Address Confirmation Email
#         current_site = get_current_site(request)
#         email_subject = "Confirm your Email @GopaljiCeation"
#         message2 = render_to_string('email_confirmation.html',{
            
#             'name': myuser.first_name,
#             'domain': current_site.domain,
#             'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
#             'token': generate_token.make_token(myuser)
#         })
#         email = EmailMessage(
#         email_subject,
#         message2,
#         settings.EMAIL_HOST_USER,
#         [myuser.email],
#         )
#         email.fail_silently = True
#         email.send()
        
#         return redirect('signup')
        
        
#     return render(request, 'authentication/signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, 'authentication/index.html',{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('signoutHome')
    
    return render(request, 'authentication/signin.html')


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('signoutHome')

def signoutHome(request):
    return render(request, 'authentication/signoutHome.html') #basic/index.html #authentication/signout.html


# def activate(request,uidb64,token):
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         myuser = User.objects.get(pk=uid)
#     except (TypeError,ValueError,OverflowError,User.DoesNotExist):
#         myuser = None

#     if myuser is not None and account_activation_token.check_token(myuser,token):
#         myuser.is_active = True
#         # user.profile.signup_confirmation = True
#         myuser.save()
#         login(request,myuser)
#         messages.success(request, "Your Account has been activated!!")
#         return redirect('signin')
#     else:
#         return render(request,'authentication/activation_failed.html')
    

def signup(request):  
    if request.method == 'POST':  
        form = SignupForm(request.POST)  
        if form.is_valid():  
            # the form has to be saved in the memory and not in DB
            user = form.save(commit=False)  
            user.is_active = False  
            user.save()  
            #This is  to obtain the current cite domain   
            current_site_info = get_current_site(request)  
            mail_subject = 'The Activation link has been sent to your email address'  
            message = render_to_string('acc_active_email.html', {  
                'user': user,  
                'domain': current_site_info.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()  
            return HttpResponse('Please proceed confirm your email address to complete the registration')  
    else:  
        form = SignupForm()  
    return render(request, 'authentication/signup.html', {'form': form})  

def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:  
        return HttpResponse('Activation link is invalid!')  