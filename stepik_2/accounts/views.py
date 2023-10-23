
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout
from .forms import CustomUserCreationForm


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def logout_view(request):
    logout(request)
    return redirect('home')


# class LogoutPageView(generic.CreateView):
#     success_url = reverse_lazy('home')
#     template_name = 'registration/logout.html'
