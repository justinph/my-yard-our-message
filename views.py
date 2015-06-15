from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.flatpages.models import FlatPage
from yardsigns.models import Sign



def main_page(request):
	#get the page content from flatpages app
	flatpage = FlatPage.objects.get(url='/')

	# get signs, return a group of 5 signs for rotation on homepage
	
	signs = Sign.objects.exclude(approved=False)
	signsCount = signs.count()	
	print signsCount
	
	
	if signsCount > 5:
		import random
		signList = random.sample(signs,5)
	else:
		signList = signs

 	
	return render_to_response('home.html',{'flatpage':flatpage,'signs':signList})	
