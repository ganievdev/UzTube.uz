from django import forms
from django.db.models.fields import FilePathField
from django.forms import fields
from main.models import Post
from django.core.validators import EmailValidator, MinLengthValidator, RegexValidator
from django.contrib.auth.validators import UnicodeUsernameValidator
from .models import User

from django.core.exceptions import ValidationError


# from mover.widgets import ImageRenderWidget

  


class RegistrationForm(forms.ModelForm):
    confirm = forms.CharField(max_length=50, widget=forms.PasswordInput)

    def clean_confirm(self):
        if self.cleaned_data['confirm']!=self.cleaned_data['password']:
            raise ValidationError("Parollar bir xil bo'lishi shart.")

        return self.cleaned_data['confirm']
    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'password', 'confirm','photo')
        
        widgets = {
            'password': forms.PasswordInput,
            'first_name':forms.TextInput(attrs={'placeholder': 'Ism'}),
            'last_name':forms.TextInput(attrs={'placeholder': 'Familya'})
        }
        

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={
                                'class':'text-white'}), )
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):

    class Meta:
        model  = User
        fields = ('first_name', 'last_name','photo')
        # widgets = {
        #     'photo': ImageRenderWidget
        # }

class PostCreateForm(forms.Form):
    subject = forms.CharField(max_length=50,
                            help_text="video yuklash",
                            widget=forms.TextInput(attrs={'placeholder': 'Mavzuni Kriting'}))

    content = forms.CharField(widget=forms.Textarea,required=False)
    video = forms.FileField(required=True)
        



    # class Meta:
    #     model = Post
    #     fields = ('subject', 'content', 'image'))





