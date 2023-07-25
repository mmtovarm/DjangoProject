from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')  
    template_name = 'users/createAccount.html'

class ProfileView(CreateView):
    model = CustomUser
    template_name = 'users/viewProfile.html/'
    context_object_name = 'viewProfile'

class ProfileView(generic.ListView):
    template_name = 'users/viewProfile.html/'
    context_object_name = "viewProfile"
    
    def get_queryset(self):
        '''Return all user data.'''
        return CustomUser.objects.all()