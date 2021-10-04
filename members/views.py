from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
import app.settings as settings


class MemberLoginView(LoginView):
    template_name = 'registration/member_login.html'

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar Sesión'
        return context
