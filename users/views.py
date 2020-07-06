from django.shortcuts import render, redirect
from django import views
from django.contrib.auth.models import User
from .forms import UserForm, ProfileForm

def GetUsers(request):
    users = User.objects.filter(is_superuser=False)#se puede poner filtro pero va a arrojar varios resultados.
    template_name="users/list.html"
    context ={
        'users':users
    }
    return render(request, template_name, context)

def GetUser(request, id):
    users = User.objects.get(pk=id)#arroja un resultado en especifico
    template_name = "users/detail.html"
    context = {
        'user': users
    }
    return render(request, template_name, context) 


class CreateUser(views.View):
    def get(self, request):
        user_form = UserForm()
        profile_form = ProfileForm()
        template_name = 'users/form.html'
        context ={
            'user_form':user_form,
            'profile_form': profile_form
        }
        return render(request, template_name, context)
    
    def post(self, request):
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password()
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('')
