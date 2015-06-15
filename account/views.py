from django.shortcuts import render_to_response
from forms import *
from django.http import HttpResponseRedirect, Http404, HttpResponse
from nesh.thumbnail.field import ImageWithThumbnailField
import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from models import MyomProfile
from django import oldforms  #for the login manipulator stuff
from django.contrib.auth.decorators import login_required

from yardsigns.models import Sign
from yardsigns.forms import DeleteSign

def register_page(request): 
	if request.user.is_authenticated(): #redircect to manage page if they're already logged in
		return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
	
	if request.GET.has_key('redirect_to'):
		if request.GET['redirect_to'] == '/submit/':
			message = "You must create an account or log in using your existing account before you can submit a sign."
		else:
			message = "You must log in before accessing your account."	
	else:
		message = None
		
	#manipulator = AuthenticationForm(request)
	regForm = None
	loginForm = None
	if request.method == 'POST':  #this means we've got form input to deal with
		if request.POST.has_key('register_form'):  #test to see which form we're submitting
			regForm = RegistrationForm(request.POST) 
			if regForm.is_valid(): 
				user = User.objects.create_user( 
					username=regForm.cleaned_data['username'], #this is actually the display name!
					password=regForm.cleaned_data['password1'], 
					email=regForm.cleaned_data['email'] 
				) 
				profile = MyomProfile.objects.create(
					user = user,
					street_address = regForm.cleaned_data['street_address'],
					city = regForm.cleaned_data['city'],
					state = regForm.cleaned_data['state'],
					country = regForm.cleaned_data['country'],
					zip = regForm.cleaned_data['zip'],
					url = regForm.cleaned_data['url']
				)
				#logs out user (if logged in), authenticates them, then logs them in as the new user
				from django.contrib.auth import login, authenticate, logout
				logout(request)
				user=authenticate(username=regForm.cleaned_data['username'], password=regForm.cleaned_data['password1'])
				login(request, user)
				return HttpResponseRedirect('/submit/') 
		else:
			regForm = RegistrationForm()   
		#logic for login form	
		if request.POST.has_key('login_form'):
			loginForm = loginWithEmailForm(request.POST)
			if loginForm.is_valid():
			
				from django.contrib.auth import login, authenticate
				tmpUser = User.objects.get(email=loginForm.cleaned_data['email'])
				authUser=authenticate(username=tmpUser.email, password=loginForm.cleaned_data['password'])
				login(request, authUser)
	
				return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)	
		else:
			loginForm = loginWithEmailForm()
		
		return render_to_response( 'account/register_or_login.html', {'regForm': regForm, 'loginForm': loginForm, 'message':message  } )
	else: 
		regForm = RegistrationForm()
		loginForm = loginWithEmailForm()

		return render_to_response( 'account/register_or_login.html', {'regForm': regForm, 'loginForm':  loginForm, 'message':message } )
		
		
# logs the user out		
def logout_page(request):
	from django.contrib.auth import logout
	logout(request)
	return HttpResponseRedirect('/')
	
	
@login_required(redirect_field_name='redirect_to')	
def manage_account(request):
	'''eventually this will have info about current signs and stuff'''
	signs = Sign.objects.filter(user=request.user)
	return render_to_response( 'account/manage.html', {'user':request.user, 'signs':signs,'settings':settings, 'delete':True} )
	
	
@login_required(redirect_field_name='redirect_to')	
def delete_sign(request,sign_id):
	'''for deleting signs'''
	sign = Sign.objects.get(id=sign_id)
	
	if sign.user_id != request.user.id:
		return HttpResponseRedirect('/account/')
	if request.method == 'POST': 
		form = DeleteSign(request.POST) 		
		if form.is_valid(): 
			sign.delete()
			return HttpResponseRedirect('/account/')
	else: 
		form = DeleteSign()	
	return render_to_response( 'account/delete_sign.html', {'user':request.user, 'sign':sign, 'form':form,'settings':settings} )	

	
	
@login_required(redirect_field_name='redirect_to')	
def update_account(request):
	'''eventually this will have info about current signs and stuff'''
	message = None
	
	if request.method == 'POST':  #this means we've got form input to deal with
	
		#way to pass the form info on the current user
		data = request.POST.copy() 
		data['user'] = request.user	
		form = UpdateRegistrationForm(data) 
		
		if form.is_valid(): 
			user = request.user
			# here, update the account with the proper forms
			user.email = form.cleaned_data['email']
			user.username = form.cleaned_data['username']
			user.save()
			
			#do stuff here to update account 
			profile = MyomProfile.objects.get(user=user)
			profile.street_address = form.cleaned_data['street_address']
			profile.city = form.cleaned_data['city']
			profile.state = form.cleaned_data['state']
			profile.country = form.cleaned_data['country']
			profile.zip = form.cleaned_data['zip']
			profile.url = form.cleaned_data['url']
			profile.save()
			
			
			message = "Your account has been updated."		
	else: 
		user = request.user
		try:
			profile = user.get_profile()			
			thePost = {
				'email': user.email,
				'username': user.username,
				'street_address': profile.street_address,
				'city': profile.city,
				'country': profile.country,
				'state': profile.state,
				'user': request.user,
				'zip': profile.zip,
				'url': profile.url,
			}
		except Exception, e:
			thePost = {'email': user.email}
		form = UpdateRegistrationForm(thePost)	
	return render_to_response( 'account/update.html', {'user':request.user,'form': form, 'message':message } )	
	
