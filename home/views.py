from django.shortcuts import render
from .models import *

def home(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def contact(request):
	if request.method == "POST": #form ma pathako value fetch garya ho
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']
		data = Contact.objects.create(
				name = name,
				email = email,
				subject = subject,
				message = message

			)
		data.save()
	
	views  = {}
	views['infos'] = Info.objects.all() # this means select all from info model

	return render(request,'contact.html',views)

def portfolio(request):
	return render(request,'portfolio.html')	

def services(request):
	return render(request,'services.html')		

def price(request):
	return render(request,'price.html')	





