from django import forms
from django.contrib.auth.models import User

from .models import UserProfile


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    company = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    website = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    city = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    province = forms.ChoiceField(choices=UserProfile.PROVINCES)
    postal_code = forms.CharField(max_length=7, widget=forms.TextInput(attrs={'class': 'form-control'}))
    private = forms.BooleanField(label="Please make my address private.", required=False)

    def clean_email(self):
        try:
            User.objects.get(username=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError("Sorry, an account currently exists with this email address.")

    def clean_password_confirmation(self):
        if 'password' in self.cleaned_data and 'password_confirmation' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password_confirmation']:
                raise forms.ValidationError("Your passwords do not match.")
        return self.cleaned_data

    def save(self):
        new_user = User(
            username = self.cleaned_data['email'],
            email = self.cleaned_data['email'],
            first_name = self.cleaned_data['first_name'],
            last_name = self.cleaned_data['last_name'],
            is_active = True
        )
        new_user.set_password(self.cleaned_data['password'])
        new_user.save()

        new_profile = UserProfile(
            user = new_user,
            company = self.cleaned_data['company'],
            address = self.cleaned_data['address'],
            province = self.cleaned_data['province'],
            city = self.cleaned_data['city'],
            postal_code = self.cleaned_data['postal_code'],
            phone = self.cleaned_data['phone'],
            website = self.cleaned_data['website'],
            private = self.cleaned_data['private'],
        )
        new_profile.save()