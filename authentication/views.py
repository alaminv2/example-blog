from django.http import Http404
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, loginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# LOGIN VIEW ENDPOINT

# def login(request):
#     return render(request, 'login.html')


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('authenticate:login')
    template_name = 'register.html'


def LoginView(request):
    form = loginForm()
    if request.method == 'POST':
        form = loginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homeee')
    return render(request, 'registration/login.html', {'form': form})


@login_required
def logoutView(request):
    logout(request)
    return redirect('authenticate:login')
