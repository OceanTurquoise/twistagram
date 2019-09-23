from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import MinLengthValidator
from django.utils.translation import ugettext_lazy

from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "icon")

    def clean_password(self):
        password = self.cleaned_data.get('password1')
        if not re.search(r'\d', password):
            raise forms.ValidationError('数字が含まれていません')
        if not re.search(r'[a-zA-Z]', password):
            raise forms.ValidationError('アルファベットが含まれていません')
        return password
