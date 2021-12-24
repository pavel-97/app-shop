from django import forms


class AdvertisementForm(forms.Form):
    title = forms.CharField(min_length=3, max_length=20)
    description = forms.CharField(widget=forms.Textarea, min_length=10, max_length=200)
    price_title = forms.FloatField(min_value=10, max_value=100000)