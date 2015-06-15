from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

	
def main_page(request):
	return render_to_response('home.html')	
