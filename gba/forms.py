from django import forms
from captcha.fields import ReCaptchaField

class AddGuBook(forms.Form):
	username = forms.CharField()
	email = forms.EmailField()
	homepage = forms.URLField(required=False)
	text = forms.CharField(widget=forms.Textarea)
	captcha = ReCaptchaField()

class RecaptchaForm(AddGuBook):
    captcha = ReCaptchaField()

