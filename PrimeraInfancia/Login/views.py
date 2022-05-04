from django.shortcuts import render
from django.contrib.auth.views import LoginView

class LoginFormView(LoginView):
    template_name= 'login.html'
    def get_cotext_data(self, **kwargs):
        context = super().get_cotext_data(**kwargs)
        context['title'] = 'Iniciar Sesión'
        return context