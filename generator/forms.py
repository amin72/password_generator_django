from django import forms


class OptionsForm(forms.Form):
    length = forms.IntegerField(initial=12)
    uppercase = forms.BooleanField(required=False)
    special_chars = forms.BooleanField(required=False)
