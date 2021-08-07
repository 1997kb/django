from django.db import models

# add data in admin panel

class Contact(models.Model):
	name = models.CharField(max_length = 300)
	email = models.CharField(max_length = 300)
	subject = models.TextField()
	message = models.TextField()

	def __str__(self):
		return self.name
# to fetch data from database
class Info(models.Model):
	address = models.CharField(max_length=300)
	local_address = models.CharField(max_length=400)
	email = models.CharField(max_length=300)
	time = models.CharField(max_length=400)
	phone = models.CharField(max_length=100,blank = True) #we need to add this if are adding a new field to this existing model


	def __str__(self):
		return self.address



