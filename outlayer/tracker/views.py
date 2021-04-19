from django.shortcuts import render
from tracker.forms import UserForm
from .models import Profile

def signup_view(request):
    if request.method == 'POST':
        form = UserFrom(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(name='user', monthly_limit=0, expenses_soFar=0)
            return redirect('login')
    else:
        form = UserForm()
    return render('registeration/signup.html',{'form':form})



