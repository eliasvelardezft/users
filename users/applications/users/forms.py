from django import forms

from .models import User

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label = 'Contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Contraseña'
            }
        )
    )
    password2 = forms.CharField(
        label = 'Repetir contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Repetir contraseña'
            }
        )
    )

    class Meta:
        model = User
        fields = ('__all__')
        fields = [
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero',
        ]
    
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'las pw son distintas')
        else:
            if len(self.cleaned_data['password1']) <= 5:
                self.add_error('password1', 'la contraseña debe tener +5 caracteres')


class LoginForm(forms.Form):    
    username = forms.CharField(
        label = 'Username',
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Contraseña'
            }
        )
    )
    password = forms.CharField(
        label = 'Contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Contraseña'
            }
        )
    )