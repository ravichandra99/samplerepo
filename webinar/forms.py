from django import forms
from django.forms import ModelForm
from webinar.models import JustUser

class UserForm(ModelForm):
	class Meta:
		model = JustUser
		fields = '__all__'

