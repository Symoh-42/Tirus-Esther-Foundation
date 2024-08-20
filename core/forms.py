from django.contrib.auth.forms import PasswordResetForm
from django import forms


class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'w-full py-3 border border-slate-200 rounded-lg px-3 focus:outline-none focus:border-slate-500 hover:shadow',
        'placeholder': 'Enter a valid email',
        
    }))

    # password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
    #     'class': 'w-full py-3 border border-slate-200 rounded-lg px-3 focus:outline-none focus:border-slate-500 hover:shadow',
    #     # 'placeholder': 'Enter a valid email',
        
    # }))