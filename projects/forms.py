from django import forms
from .models import *


class projectForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        error_messages={"invalid": ("Enter your name")},
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-bl-3xl rounded-tr-3xl focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }
        ),
    )

    description = forms.CharField(
        required=True,
        error_messages={"invalid": ("Enter your description")},
        widget=forms.Textarea(
            attrs={
                "class": "block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-bl-3xl rounded-tr-3xl border border-gray-300 focus:ring-blue-500 focus:border-blue-500",
            }
        ),
    )

    completed = forms.CharField(
        required=False,
        error_messages={"invalid": ("Enter your active")},
        widget=forms.CheckboxInput(
            attrs={
                "class": "w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded md focus:ring-blue-500 focus:ring-2",
            }
        ),
    )

    in_progress = forms.CharField(
        required=False,
        error_messages={"invalid": ("Enter your active")},
        widget=forms.CheckboxInput(
            attrs={
                "class": "w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded md focus:ring-blue-500 focus:ring-2",
            }
        ),
    )
    active = forms.CharField(
        required=False,
        error_messages={"invalid": ("Enter your active")},
        widget=forms.CheckboxInput(
            attrs={
                "class": "w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded md focus:ring-blue-500 focus:ring-2",
            }
        ),
    )

    youtube_link = forms.CharField(
        required=False,
        error_messages={"invalid": ("Enter your position")},
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-bl-3xl rounded-tr-3xl focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }
        ),
    )

    main_image = forms.ImageField(
        required=True,
        error_messages={"invalid": ("Image files only")},
        widget=forms.FileInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-bl-3xl rounded-tr-3xl focus:ring-blue-500 focus:border-blue-500 block w-full",
            }
        ),
    )

    def clean_name(self):
        title = self.cleaned_data.get("title")
        if len(title) < 3:
            raise forms.ValidationError("title must be at least 3 characters long.")
        return title

    class Meta:
        model = Project
        fields = "__all__"
        


class projectImagesForm(forms.ModelForm):
    other_project_images = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        
    )

    class Meta:
        model = OtherProjectImages
        fields = ["other_project_images"]

    def __init__(self, *args, **kwargs):
        super(projectImagesForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields["other_project_images"].widget.attrs[
                "class"
            ] = "shadow-sm rounded-tr-3xl rounded-bl-3xl bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm focus:ring-yellow-600 focus:border-yellow-600 block w-full"

