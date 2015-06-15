from django.shortcuts import render_to_response
from models import Sign, Tag
from forms import *
from django.http import HttpResponseRedirect
from PIL import Image 			#bring in the image library to test the image
import StringIO

def add_sign(request):
	

	if request.method == "POST":
		post_data = request.POST.copy()
		post_data.__setitem__('submitter_ip',request.META['REMOTE_ADDR'])
		print post_data	
		form = SignForm(post_data,request.FILES)
		if form.is_valid():
			form.save()
			print form
			return HttpResponseRedirect('/submit/thanks/')
		
	else:
		form = SignForm()
		
	return render_to_response('yardsigns/submit.html',{"form":form})	
	
	
def sign_thanks(request):
	return render_to_response('yardsigns/thanks.html')