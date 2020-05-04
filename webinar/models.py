from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class JustUser(models.Model):
	#just_id = models.CharField(max_length = 100)
	fname = models.CharField(max_length = 30,verbose_name = 'First Name')
	lname = models.CharField(max_length = 30,verbose_name = 'Last Name')
	email = models.EmailField(unique = True)
	mobile = PhoneNumberField(unique = True)
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

class Webinar(models.Model):
	title = models.CharField(max_length = 100)
	image = models.ImageField(upload_to = '')
	link = models.URLField()

	def __str__(self):
		return self.title
