from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import EmailField, ModelForm, ClearableFileInput, Textarea, URLInput

from registration.models import Profile


class UserCreationFormWithEmail(UserCreationForm):
    email = EmailField(required=True, help_text="Obligatorio")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("El email ya está registrado")
        return email


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': ClearableFileInput(
                attrs={'class': 'form-control-file mt-3'}
            ),
            'bio': Textarea(
                attrs={
                    'class': "form-control mt-3", 'rows': 3, 'placeholder': "Biografía"
                }
            ),
            'link': URLInput(
                attrs={
                    'class': "form-control mt-3", 'rows': 3, 'placeholder': "Enlace"
                }
            )
        }


class EmailForm(ModelForm):
    email = EmailField(required=True, help_text="Obligatorio")

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise ValidationError("El email ya está registrado")
        return email
