from django.urls impoprt path
from .views import *

urlpatterns = [
	path('',home,name='home'),
	path('about',about,name='about')
	

	
]