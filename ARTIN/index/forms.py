from django import forms

from index.models import Contactform


class Contact_Form(forms.ModelForm):
    class Meta:
        model = Contactform
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'نام و نام خوانوادگی'}),
            'email': forms.TextInput(attrs={'placeholder': 'ایمیل'}),
            'subject': forms.TextInput(attrs={'placeholder': 'موضوع'}),
            'phone': forms.TextInput(attrs={'placeholder': 'شماره تماس'}),
            'description': forms.Textarea(attrs={'placeholder': 'پیام خود را وارد کنید'}),
        }
        fields = [
            'name',
            'email',
            'subject',
            'phone',
            'description',
        ]
