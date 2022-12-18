from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['username'].help_text=''
      self.fields['email'].help_text=''
      self.fields['password1'].help_text=''
      self.fields['password2'].help_text=''

class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text=''
        self.fields['password'].help_text=''

