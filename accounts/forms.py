from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm, CharField

User = get_user_model()


class ReistrationForm(ModelForm):
    password1 = forms.CharField(label="pass", widget=forms.PasswordInput())
    password2 = forms.CharField(label="pass_confirm", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', ]

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("password do not match")
        return password2

    def clean_email(self):
        email = self.cleaned_data.get("email")
        user_count = User.objects.filter(email=email).count()
        print
        user_count
        if user_count > 0 and email:
            raise forms.ValidationError("this email is signed up before")
        return email

    def save(self, commit=True):
        user = super(ReistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
