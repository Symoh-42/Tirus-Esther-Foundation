from django import forms
from .models import *

class StoryCardForm(forms.ModelForm):
    active = forms.CharField(
        required=True,
        error_messages={"invalid": ("Enter your active")},
        widget=forms.CheckboxInput(
            attrs={
                "class": "w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded mdcus:ring-blue-500 focus:ring-2",
            }
        ),
    )

    image = forms.ImageField(
        required=True,
        error_messages={"invalid": ("Image files only")},
        widget=forms.FileInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-bl-3xl rounded-tr-3xl shadow focus:ring-blue-500 focus:border-blue-500 block w-full",
            }
        ),
    )

    name = forms.CharField(
        required=True,
        error_messages={"invalid": ("Enter your name")},
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-bl-3xl rounded-tr-3xl shadow focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }
        ),
    )

    description = forms.CharField(
        required=True,
        error_messages={"invalid": ("Enter your massage")},
        widget=forms.Textarea(
            attrs={
                "class": "block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-bl-3xl rounded-tr-3xl shadow border border-gray-300 focus:ring-blue-500 focus:border-blue-500",
            }
        ),
    )

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long.")
        return name

    class Meta:
        model = StoryCard
        fields = "__all__"