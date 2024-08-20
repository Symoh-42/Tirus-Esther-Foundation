from django.forms import ModelForm
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import *


class blogForm(ModelForm):
    cover_image = forms.ImageField(
        required=True,
        error_messages={"invalid": ("Image files only")},
        widget=forms.FileInput,
    )
    blog_description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = BlogPost
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(blogForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs[
                "class"
            ] = "block w-full px-4 py-2 text-gray-700 bg-white border rounded-bl-3xl rounded-tr-3xl border border-gray-200 focus:border-black focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40"
            
            self.fields["cover_image"].widget.attrs[
                "class"
            ] = "block w-full px-4 text-gray-700 bg-white border rounded-bl-3xl rounded-tr-3xl border border-gray-200 focus:border-black focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40"
            
            self.fields["featured"].widget.attrs[
                "class"
            ] = "w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 focus:ring-2"

            self.fields["published"].widget.attrs[
                "class"
            ] = "w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 focus:ring-2"

class CommentForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        error_messages={"invalid": ("Enter your name")},
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-bl-3xl rounded-tr-3xl shadow-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }
        ),
    )

    comment = forms.CharField(
        required=True,
        error_messages={"invalid": ("Enter comment")},
        widget=forms.Textarea(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-bl-3xl rounded-tr-3xl shadow-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }
        ),
    )

    class Meta:
        model = Comments
        fields = ["name", "comment"]
            