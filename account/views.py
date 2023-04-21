from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from .forms import UserRegistrationForm

# Create your views here.

class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'account/register.html', {
            'form': form
            })
    
    def post(self, request):
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            authenticate(username = user.username, password = user.password)
            
            if user is not None:
                login(request, user)
                
                return redirect('index')
        else:
            form = UserRegistrationForm()
            