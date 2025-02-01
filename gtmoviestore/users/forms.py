from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django import forms
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model

class CustomErrorList(ErrorList):
    def __str__(self):
        if not self:
            return ''
        return mark_safe(''.join([
            f'<div class="alert alert-danger" role="alert">{e}</div>' for e in self]))

#ChatGPT used for email functionality
class CustomUserCreationForm(UserCreationForm):

    email = forms.EmailField(required=True)  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['username', 'password1','password2','email']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update(
                {'class': 'form-control'}
                )
            
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2','email']

