from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=User.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'password1', 'password2')
        help_texts = {
            'username': "",
            'password1': "",
            'password2': "",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'style': 'height: 42px;'
            })


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control', 'style': 'height: 42px;'})
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'height: 42px;'})
    )