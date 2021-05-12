from django.shortcuts import render, redirect
from tracker.forms import UserForm
#from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Records
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

def signup_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
            Profile.objects.create(name=user, monthly_limit=0, expenses_soFar=0)
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'registration/signup.html',{'form':form})

def login_view(request):
        if request.method == 'POST':
           form= AuthenticationForm(data=request.POST)
           if form.is_valid():
               user=form.get_user()
               login(request,user)
               return redirect('home', username=user.username)
        else:
            form=AuthenticationForm()
        return render(request, 'registration/login.html',{'form':form})

def logout_view(request):
         logout(request)
         return redirect('login')



def additem_view(request):
    expense_name = request.POST['expense_name']
    expense_cost = request.POST['expense_cost']
    expense_date = request.POST['expense_date']
    expense_type = request.POST['expense_type']
    Records.objects.create(expenditure_user= request.user, 
                           expenditure_name=expense_name, 
                           expenditure_amount=expense_cost, 
                           expenditure_type=expense_type, 
                           expenditure_date=expense_date)
    user_qs = Profile.objects.filter(name=request.user)
    user_obj = user_qs[0]
    total = user_obj.expenses_soFar
    total+= float(expense_cost)
    user_obj.expenses_soFar = total
    user_obj.save(update_fields=['expenses_soFar'])
    return HttpResponseRedirect(reverse('home', kwargs={'username':request.user}))
       
def home_view(request, username):
    if request.user.is_authenticated:
        print(request.user)
        budget_qs = Profile.objects.filter(name=request.user)
        uzer_qs = Records.objects.filter(expenditure_user=request.user).order_by('-expenditure_date')
        return render(request,'home/home.html',{'budget':request.user,'uzer':uzer_qs[0:7]})
    else:
        return render(request,'home/home.html')


def profile_view(request):
	if request.method=="GET":
		return render(request,'home/profile.html')
	if request.method=="POST":
		uzer_qs = Profile.objects.filter(name=request.user)
		uzer_obj = uzer_qs[0]
		incm = uzer_obj.monthly_limit
		incm = request.POST['income']
		uzer_obj.monthly_limit = incm
		uzer_obj.save(update_fields=['monthly_limit'])
		return redirect('profile',username=request.user)

# Both HttpResponseRedirect(reverse(...)) and redirect(... , ...) works fine


