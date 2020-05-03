from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class JustUser(models.Model):
	fname = models.CharField(max_length = 30,verbose_name = 'First Name')
	lname = models.CharField(max_length = 30,verbose_name = 'Last Name')
	email = models.EmailField()
	mobile = PhoneNumberField()
	college = models.CharField(max_length = 30,verbose_name = 'College/Organization')
	profession = models.CharField(max_length = 30,verbose_name = 'Profession')

	def __str__(self):
		return self.fname+' '+self.lname

class JustEdit(models.Model):
	ref = models.CharField(max_length = 4)
	subject = models.CharField(max_length = 100)
	body = models.TextField()

	def __str__(self):
		return self.ref