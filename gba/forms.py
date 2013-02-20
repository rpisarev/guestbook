from django import forms
from captcha.fields import ReCaptchaField
import re

class AddGuBook(forms.Form):
	username = forms.CharField()
	email = forms.EmailField()
	homepage = forms.URLField(required = False)
	text = forms.CharField(widget = forms.Textarea)
	image = forms.ImageField(required = False)
	captcha = ReCaptchaField()

	def clean_username(self):
		username = self.cleaned_data['username']
		regexp_name = re.compile('[a-zA_Z0-9]+')
		if regexp_name.match(username).group() != username:
			raise forms.ValidationError("Not digits or alphabetic!")
		return username
	def clean_text(self):
		text = self.cleaned_data['text']
		if text.find('<') > -1 or text.find('lt;') > -1:
			raise forms.ValidationError("HTML-tag baned!")
		return text


class RecaptchaForm(AddGuBook):
    captcha = ReCaptchaField()

