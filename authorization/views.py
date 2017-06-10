from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = 'authorization/login.html'


class RegisterView(TemplateView):
    template_name = 'authorization/register.html'
