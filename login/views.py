from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



# For login...
def login_form(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in Successfully !!")
                    return HttpResponseRedirect('/my_profile/')
        else:    
            fm = LoginForm()
        
        return render(request, 'login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/my_profile/')    

# for profile..
def profile(request):
    if request.user.is_authenticated:
       return render(request, 'my_profile.html')
    else:
       return HttpResponseRedirect('/')     

# for logout...
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')   
  

 
#For sign up..
def sign_up(request):
    if request.method == 'POST':
      fm = SignUpForm(request.POST)
      if fm.is_valid():
        fm.save()
    else:    
        fm = SignUpForm()
    return render(request, 'sign_up.html', {'form': fm})    