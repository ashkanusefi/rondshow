from django import forms
from django.forms import DateInput

from account.models import Profile
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["mobile", "GENDER", "address", "birth_date", "profile_image"]


class MyUserForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ["first_name", "last_name", "email", "username"]

    password = None


class SignUpForm(UserCreationForm):
    mobile = forms.CharField(max_length=12)
    address = forms.CharField(max_length=500)
    MALE = 1
    FEMALE = 2
    GENDER_CHOICE = ((MALE, "مرد"), (FEMALE, "زن"))
    GENDER = forms.ChoiceField(choices=GENDER_CHOICE)
    birth_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    profile_image = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['mobile'].label = "شماره موبایل"
        self.fields['address'].label = "ادرس"
        self.fields['birth_date'].label = "تاریخ تولد"
        self.fields['GENDER'].label = "جنسیت"
        self.fields['profile_image'].label = "عکس پروفایل"

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'mobile', 'address', 'GENDER', 'birth_date','profile_image']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            Profile.objects.create(address=self.cleaned_data["address"],
                                   mobile=self.cleaned_data["mobile"],
                                   GENDER=self.cleaned_data["GENDER"],
                                   birth_date=self.cleaned_data["birth_date"],
                                   profile_image=self.cleaned_data["profile_image"],
                                   user=user)
        return user
