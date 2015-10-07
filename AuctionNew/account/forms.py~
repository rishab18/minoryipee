from django import forms
from django.contrib.auth import authenticate
from .models import MyUser
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length = 254)
    password = forms.CharField(widget = forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            self.user_cache = authenticate(username = username, password = password)
            if self.user_cache is None:
                raise forms.ValidationError('Please enter a correct username and password')
            elif not self.user_cache.is_active:
                raise forms.ValidationError('This account is inactive')
        return self.cleaned_data
    def get_user(self):
        return self.user_cache

class SignupForm(forms.ModelForm):
    password1 = forms.CharField(label = "Password", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Confirm Password", widget = forms.PasswordInput, help_text = " Enter the same password as above")
#    placeHolderField = forms.CharField(label="Placeholder Field", widget = forms.TextInput(attrs={'placeholder' : 'myplace holder text', 'class' : 'myclass'}))
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean_email(self):
        email_data = self.cleaned_data.get("email")
        if email_data and len(MyUser.objects.filter(email = email_data)) > 0:
            raise forms.ValidationError("User with this email already exist")
        return email_data

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['phone'].required = True

    def save(self, commit = True):
        user  = super(SignupForm, self).save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'phone']


class ForgotPasswordForm(PasswordResetForm):
    def clean_email(self):
       email = self.cleaned_data.get('email')
       if email and MyUser.objects.filter(email = email).count() == 0:
           raise forms.ValidationError("We cannot find account with this email. Please verify your email address and try again.")
       return email

class ResetPasswordForm(SetPasswordForm):
    def __init__(self, user, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(user, *args, **kwargs)
        self.fields['new_password2'].label = 'Confirm Password'
