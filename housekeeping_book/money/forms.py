from django import forms
from .models import Money

class SpendingForm(forms.Form):
    use_date = forms.DateTimeField(label='日付')
    cost = forms.IntegerField(label='金額')
    detail = forms.CharField(
            max_length=200,
            label='用途'
            )