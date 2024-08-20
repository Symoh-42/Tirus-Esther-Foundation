from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class TestimonialForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        error_messages={"invalid": ("Enter your name")},
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-bl-3xl rounded-tr-3xl shadow focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }
        ),
    )

    message = forms.CharField(
        required=True,
        error_messages={"invalid": ("Enter your massage")},
        widget=forms.Textarea(
            attrs={
                "class": "block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-bl-3xl rounded-tr-3xl shadow border border-gray-300 focus:ring-blue-500 focus:border-blue-500",
            }
        ),
    )

    active = forms.CharField(
        required=False,
        error_messages={"invalid": ("Enter your active")},
        widget=forms.CheckboxInput(
            attrs={
                "class": "w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded mdcus:ring-blue-500 focus:ring-2",
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
        model = Testimonial
        fields = "__all__"


class TeamForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        error_messages={"invalid": ("Enter your name")},
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-bl-3xl rounded-tr-3xl shadow focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }
        ),
    )
    position = forms.CharField(
        required=True,
        error_messages={"invalid": ("Enter your position")},
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-bl-3xl rounded-tr-3xl shadow focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
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

    description = forms.CharField(
        required=True,
        error_messages={"invalid": ("Enter your description")},
        widget=forms.Textarea(
            attrs={
                "class": "block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-bl-3xl rounded-tr-3xl shadow border border-gray-300 focus:ring-blue-500 focus:border-blue-500",
            }
        ),
    )

    active = forms.CharField(
        error_messages={"invalid": ("Enter your active")},
        widget=forms.CheckboxInput(
            attrs={
                "class": "w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded md focus:ring-blue-500 focus:ring-2",
            }
        ),
    )

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long.")
        return name

    class Meta:
        model = Team
        fields = "__all__"


class SponsorForm(forms.ModelForm):
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

    link = forms.CharField(
        required=True,
        error_messages={"invalid": ("Enter valid link")},
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
        model = Sponsor
        fields = "__all__"


class settingsForm(forms.ModelForm):
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-bl-3xl rounded-tr-3xl shadow focus:ring-sky-500 focus:border-sky-500 block w-full p-2.5",
            }
        ),
    )

    phone2 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-bl-3xl rounded-tr-3xl shadow focus:ring-sky-500 focus:border-sky-500 block w-full p-2.5",
            }
        ),
    )

    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-bl-3xl rounded-tr-3xl shadow focus:ring-sky-500 focus:border-sky-500 block w-full p-2.5",
            }
        ),
    )

    google_map = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-bl-3xl rounded-tr-3xl shadow focus:ring-sky-500 focus:border-sky-500 block w-full p-2.5",
            }
        ),
    )

    mail_account = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-bl-3xl rounded-tr-3xl shadow focus:ring-sky-500 focus:border-sky-500 block w-full p-2.5",
            }
        ),
    )

    main_logo = forms.ImageField(
        required=True,
        error_messages={"invalid": ("Image files only")},
        widget=forms.FileInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-bl-3xl rounded-tr-3xl shadow focus:ring-blue-500 focus:border-blue-500 block w-full",
            }
        ),
    )

    about = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "h-32 block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-bl-3xl rounded-tr-3xl shadow border border-gray-300 focus:ring-sky-500 focus:border-sky-500"
            }
        ),
    )

    vision = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "h-32 block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-bl-3xl rounded-tr-3xl shadow border border-gray-300 focus:ring-sky-500 focus:border-sky-500"
            }
        ),
    )

    mission = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "h-32 block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-bl-3xl rounded-tr-3xl shadow border border-gray-300 focus:ring-sky-500 focus:border-sky-500"
            }
        ),
    )
    
    objectives = forms.CharField(
        widget=CKEditorUploadingWidget(
            attrs={
                "class": "h-32 block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-bl-3xl rounded-tr-3xl shadow border border-gray-300 focus:ring-sky-500 focus:border-sky-500"
            }
        ),
    )

    core = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "h-32 block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-bl-3xl rounded-tr-3xl shadow border border-gray-300 focus:ring-sky-500 focus:border-sky-500"
            }
        ),
    )

    facebook = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-bl-3xl rounded-tr-3xl shadow focus:ring-sky-500 focus:border-sky-500 block w-full p-2.5",
            }
        ),
    )

    tiktok = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-bl-3xl rounded-tr-3xl shadow focus:ring-sky-500 focus:border-sky-500 block w-full p-2.5",
            }
        ),
    )

    instagram = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-bl-3xl rounded-tr-3xl shadow focus:ring-sky-500 focus:border-sky-500 block w-full p-2.5",
            }
        ),
    )

    twitter = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-bl-3xl rounded-tr-3xl shadow focus:ring-sky-500 focus:border-sky-500 block w-full p-2.5",
            }
        ),
    )

    youtube = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-bl-3xl rounded-tr-3xl shadow focus:ring-sky-500 focus:border-sky-500 block w-full p-2.5",
            }
        ),
    )

    pinterest = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-bl-3xl rounded-tr-3xl shadow focus:ring-sky-500 focus:border-sky-500 block w-full p-2.5",
            }
        ),
    )

    # def clean_name(self):
    #     name = self.cleaned_data.get("name")
    #     if len(name) < 3:
    #         raise forms.ValidationError("Name must be at least 3 characters long.")
    #     return name

    class Meta:
        model = Settings
        fields = "__all__"

