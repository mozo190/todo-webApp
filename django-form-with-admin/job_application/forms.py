from django import forms


class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    resume = forms.FileField()
    cover_letter = forms.CharField(widget=forms.Textarea)
    occupation = forms.CharField(max_length=100)
