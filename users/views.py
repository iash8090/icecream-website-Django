from django.shortcuts import render,HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User

# Create your views here.

def register(request):
# We didn't create the register Class inside Models.py for this function because we are reusing predefined 'auth_user' table provided by Django to store required user details.
    try:
        if request.method == 'POST':
            fname = request.POST['fname']
            lname = request.POST.get('lname')
            uname = request.POST.get('uname')
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if (password1 == password2):
                if (not User.objects.filter(username=uname).exists()):
                    if (not User.objects.filter(email=email).exists()):
                        user = User.objects.create_user(username=uname, password=password1, email=email, first_name=fname, last_name=lname )
    # 'first_name', 'last_name' etc are already defined column name in 'auth_user' table
                        user.save()
                        messages.success(request,'You Are Registered Successfully!')
                        return redirect('/users/login')
                    else:
                        messages.info(request, 'Email Already registered')
                        return render(request, 'register.html')
                else:
                    messages.info(request, 'Username Already Exist')
                    return render(request, 'register.html')
            else:
                messages.info(request, 'Password Mismatch')
                return render(request, 'register.html')
        else:
            return render(request, 'register.html')
    except:
        pass 



def loginCustomer(request):
    try:
        if request.method=="POST":
            username = request.POST['Username']
            Pass = request.POST.get('Password')
            user = authenticate(username=username, password=Pass)
            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                messages.info(request,f"Welcome {username}! ")
                return redirect("/")
    #        elif request.user.is_anonymous:
    #            return redirect("/login")
            else:
                # No backend authenticated the credentials
                messages.error(request,"Invalid username or password.")
                return render(request,'login.html')

        return render(request,'login.html')
# user/password= testing/temporary123
    except:
        pass


def logoutCustomer(request):
    try:
        if request.user.is_anonymous:
            return redirect("/users/login")
        else:
            logout(request)
            messages.success(request,"Logged Out Successfully!")
        return redirect("/users/login")
    except:
        pass
