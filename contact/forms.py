from django import forms
# from captcha.fields import ReCaptchaField 
# from captcha.widgets import ReCaptchaV2Checkbox
from .models import *


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        error_messages={"invalid": ("Enter your name")},
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-bl-3xl rounded-tr-3xl focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }
        ),
    )

    phone = forms.CharField(
        required=True,
        error_messages={"invalid": ("Enter your phone_number")},
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-bl-3xl rounded-tr-3xl focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }
        ),
    )

    email = forms.EmailField(
        required=True,
        error_messages={"invalid": ("Enter your email")},
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-bl-3xl rounded-tr-3xl focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }
        ),
    )

    message = forms.CharField(
        required=True,
        error_messages={"invalid": ("Enter your massage")},
        widget=forms.Textarea(
            attrs={
                "class": "block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-bl-3xl rounded-tr-3xl border border-gray-300 focus:ring-blue-500 focus:border-blue-500",
            }
        ),
    )

    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long.")
        return name

    class Meta:
        model = Contact
        fields = "__all__"
