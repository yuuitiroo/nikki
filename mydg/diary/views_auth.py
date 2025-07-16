from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.shortcuts import render, redirect

class SignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registration/signup.html", {"form" : form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        return render(request, "registration/signup.html", {"form" : form})