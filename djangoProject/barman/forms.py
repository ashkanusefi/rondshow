from barman.models import Data_form
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Data_form
        fields = [
            'name',
            'email',
            'phone',
            'description',
        ]
