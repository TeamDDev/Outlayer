from django.shortcuts import render
from tracker.forms import UserForm

def signup_view(request):
    if request.method == 'POST':
        form = UserFrom(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
