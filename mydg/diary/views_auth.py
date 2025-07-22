from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()

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
    
class DeleteAccountView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "registration/delete_account.html"
    success_url = reverse_lazy("login")

    def get_object(self):
        return self.request.user
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, "アカウント削除しました。")
        return super().delete(request, *args, **kwargs)