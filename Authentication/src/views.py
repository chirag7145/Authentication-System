from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    count = User.objects.count()
    return render(request,'index.html',{'count':count})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form' : form})

@login_required
def secret(request):
    return render(request,'secret_page.html')


class Secret_Page(LoginRequiredMixin,TemplateView):
    template_name = "secret_page.html"
