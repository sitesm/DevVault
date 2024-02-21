from django import forms 

class SCDownload(forms.Form):
    scURL = forms.CharField()