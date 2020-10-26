from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import TextInput, PasswordInput, EmailInput
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView, UpdateView

from registration.forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from registration.models import Profile


class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    # success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + "?register"

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        # Modificar en tiempo de ejecución
        form.fields['username'].widget = TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre de usuario'})
        form.fields['email'].widget = EmailInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Correo Electrónico'})
        form.fields['password1'].widget = PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Contraseña'})
        form.fields['password2'].widget = PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Repite la contraseña'})
        return form


@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm

    success_url = reverse_lazy('profile')
    template_name = "registration/profile_form.html"

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile



@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm

    success_url = reverse_lazy('profile')
    template_name = "registration/profile_email_form.html"

    def get_object(self):
        # profile, created = Profile.objects.get_or_create(user=self.request.user)
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        # Modificar en tiempo de ejecución
        form.fields['email'].widget = EmailInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Correo Electrónico'})
        return form

