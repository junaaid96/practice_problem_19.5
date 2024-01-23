from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "Account Created Successfully!")
            return redirect('login')
    else:
        register_form = RegisterForm()
    return render(request, 'register.html', {'form': register_form})


class UserLogin(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, "Logged In Successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid Data!")
        return super().form_invalid(form)


@method_decorator(login_required, name='dispatch')
class UserLogoutView(LogoutView):
    # next_page = reverse_lazy('user_login')
    def get_success_url(self):
        messages.success(self.request, "Logged Out Successfully!")
        return reverse_lazy('home')
