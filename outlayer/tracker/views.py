from django.shortcuts import render, redirect
from tracker.forms import UserForm
#from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Records
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

def signup_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
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

        
def home_view(request, username):
    if request.user.is_authenticated:
        budget_qs = Profile.objects.filter(name=request.user)
        uzer_qs = Records.objects.filter(expenditure_user=request.user).order_by('-expenditure_date')
        if budget_qs or uzer_qs:
            return render(request,'home/home.html',{'budget':budget_qs[0],'uzer':uzer_qs[0:5]})
        else:
            budget_qs = [0]
            uzer_qs = [0]
            return render(request,'home/home.html',{'budget':budget_qs[0],'uzer':uzer_qs[0:5]})
    else:
        return render(request,'home/home.html')

def profile_view(request, username):
	if request.method=="GET":
		return render(request,'tasks_notes/app.html')
	if request.method=="POST":
		uzer_qs = UserInfo.objects.filter(name=request.user)
		uzer_obj = uzer_qs[0]
		incm = uzer_obj.income
		incm = request.POST['income']
		uzer_obj.income = incm
		uzer_obj.save(update_fields=['income'])
		return redirect('app',username=request.user)

# Both HttpResponseRedirect(reverse(...)) and redirect(... , ...) works fine


