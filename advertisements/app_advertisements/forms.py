from django import forms
from .models import Advertisement
from django.core.exceptions import ValidationError


# class AdvertisementForm(forms.Form):
#     title = forms.CharField(max_length=64,widget=forms.TextInput(attrs={"class":"form-control form-control-lg"}))
#     description = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control form-control-lg"}))
#     price = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control form-control-lg"}))
#     auction = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class":"form-check-input"}),required=False)
#     image = forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control form-control-lg"}),required=False)

class AdvertisementForm(forms.ModelForm):
    title = forms.CharField(
        max_length=64,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg"}),
        validators="?"
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={"class":"form-control form-control-lg"}),
        required = True
    )

    price = forms.DecimalField(
        widget=forms.NumberInput(attrs={"class":"form-control form-control-lg"}),
        required=True
    )

    auction = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
        required=False
    )

    image = forms.ImageField(
        widget=forms.FileInput(attrs={"class":"form-control form-control-lg"}),
        required=False
    )
    class Meta:
        model = Advertisement
        fields = ['title','description','price','auction','image']

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.startwith('?'):
            raise ValidationError('Заголовок не может начинаться с вопросительного знака')
        return title