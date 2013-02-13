from django import forms

class AddGuBook(forms.Form):
	username = forms.CharField()
	email = forms.EmailField()
	homepage = forms.URLField(required=False)
	text = forms.CharField(widget=forms.Textarea)

