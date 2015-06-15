from django.shortcuts import render_to_response
from models import Sign
from forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from nesh.thumbnail.field import ImageWithThumbnailField
import settings
from django.contrib.auth.models import User

from django.core.paginator import Paginator, InvalidPage

def add_sign(request):
	
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/account/register/?redirect_to=/submit/')
		
	userSigns = Sign.objects.filter(user=request.user)
	if len(userSigns) > 4:  # limit people to no more than 5 signs
		return render_to_response('yardsigns/submit.html',{'maxedOut': True,'user': request.user})
		
	if request.method == "POST":
		form = SignForm(request.POST,request.FILES)
		if form.is_valid():
			newSign = Sign(
				user = request.user,
				title = form.cleaned_data['title'],
				description = form.cleaned_data['description'],
				#image = form.cleaned_data['image'],
				accept_terms = form.cleaned_data['accept_terms'],
				submitter_ip = request.META['REMOTE_ADDR']
			)
			
			if form.cleaned_data['image']:
				image = form.cleaned_data['image']
				newSign.save_image_file(image.filename, image.content)
			newSign.save()
			goTo = '/submit/thanks/?id=' + str(newSign.id)
			return HttpResponseRedirect(goTo)
	else:
		form = SignForm()
	return render_to_response('yardsigns/submit.html',{"form":form,'user': request.user})	
	
	
def sign_thanks(request):
	if request.GET.has_key('id'):
		sign_id = request.GET['id']
	else:
		sign_id = False
	return render_to_response('yardsigns/thanks.html',{'user': request.user,'sign_id':sign_id})
	
	
def view_scroll(request,curPage=1):
	paginator = Paginator(Sign.objects.exclude(approved=False).order_by('-time_added'), 3)

	p = paginator.page(curPage)

	return render_to_response('yardsigns/view_scroll.html',{'p':p,'paginator':paginator,'settings':settings})	
	
	
def view_thumbs(request,curPage=1):
	paginator = Paginator(Sign.objects.exclude(approved=False).order_by('-time_added'), 12)

	p = paginator.page(curPage)
	
	return render_to_response('yardsigns/view_thumbs.html',{'p':p,'paginator':paginator,'settings':settings})
	
	
	
def view_sign(request,id):
	sign = get_object_or_404(Sign,id=id)
	user = User.objects.get(id=sign.user_id)
	
	#logic to make it so we can jump back to wherever we came from, so long as it's myom...
	previous = '/signs/'
	if request.META.has_key('HTTP_REFERER'):
		referer = request.META['HTTP_REFERER']
		if referer.find(request.META['SERVER_NAME']) != -1:
			previous = referer
		
	return render_to_response('yardsigns/view_single.html',{'sign':sign,'user':user,'settings':settings,'previous':previous})
	
	
def view_sign_embed(request,id):
	sign = get_object_or_404(Sign,id=id)
	user = User.objects.get(id=sign.user_id)

	return render_to_response('yardsigns/view_single_embed.html',{'sign':sign,'user':user,'settings':settings})
	
