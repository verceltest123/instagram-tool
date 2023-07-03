from django import forms

class MyForm(forms.Form):
    input_text = forms.CharField(label='Instagram link')