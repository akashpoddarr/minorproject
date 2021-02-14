from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



def handlesignup(request):

   

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for anny error
        if pass1 != pass2:
            messages.error(request, 'your passwords do not match')
            return redirect('/')
        
        #create the user
        myuser = User.objects.create_user(username=username, password=pass1)
        myuser.user_name = username
        myuser.pass_word = pass1
        myuser.save()
        messages.success(request,'your account has been created successfully!!')
        
        return redirect('/')
    else:
        return HttpResponse('404 not found! ')

def handlelogin(request):
    if request.method == 'POST':
        #get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request, 'You Have Been Successfully Logged In!!!')
            return redirect('/')
        else:
            messages.error(request, 'You Have Entered Invalid Credentials, Please Try Again!!!')

        return redirect('/')
    return HttpResponse("404 not found")

def handlelogout(request):
        logout(request)
        messages.success(request, 'You Have successfully logged out')
        return redirect('/')