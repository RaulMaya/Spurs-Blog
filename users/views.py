from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        context = {'form':form}
        
        return render(request, "registration/register.html", context)

    def post(self, request):
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            print(new_user)
            login(request, new_user)
            return redirect("blog:starting_page")
        
        context = {'form':form}
        return render(request, "registration/register.html", context)