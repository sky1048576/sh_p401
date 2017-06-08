__author__ = 'shahab'
from django import forms
from .models import Home,Picture

ostan = (
    ('1', 'esfahan'),
    ('2', 'khoozestan'),
    ('3', 'khorasan'),
)
class HomeForm(forms.ModelForm):
    # ostan = forms.ChoiceField(choices=ostan,label="witch state",)
    class Meta:
        model = Home
        fields = ['name','address', 'about','zip_code']
    def save(self,commit=True):
        _home= super(HomeForm,self).save(commit=False)
        if commit:
            _home.save()
        return _home

class ImageForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['image',]

