from django import newforms as forms
import re  #regex library
from django.contrib.auth.models import User 
from django.core.exceptions import ObjectDoesNotExist
from choices import *




class RegistrationForm(forms.Form): 
	email = forms.EmailField(label='E-mail address') 
	password1 = forms.CharField( label='Password', widget=forms.PasswordInput() ) 
	password2 = forms.CharField( label='Password (Again)', widget=forms.PasswordInput() )
	username = forms.CharField(label='Display name', max_length=30) 
	street_address = forms.CharField(required=False)
	city = forms.CharField()
	state = forms.ChoiceField(required=True,choices=STATE_CHOICES)
	country = forms.ChoiceField(required=True,choices=COUNTRY_CHOICES)
	zip = forms.CharField(label="Zip code", max_length=5,required=False)
	url = forms.URLField(label="Your web site", max_length=200,required=False)
	
	# makes sure the passwords match
	def clean_password2(self): 
		if 'password1' in self.cleaned_data: 
			password1 = self.cleaned_data['password1'] 
			password2 = self.cleaned_data['password2'] 
			if password1 == password2: 
				return password2 
			raise forms.ValidationError('Passwords do not match.') 

	# makes sure the username is unique
	def clean_username(self): 
		username = self.cleaned_data['username'] 
		# if not re.search(r'^\w+$', username): 
		# 		raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.') 
		try: 
			User.objects.get(username=username) 
		except ObjectDoesNotExist: 
			return username 
		raise forms.ValidationError('That display name is already taken.') 
	
	def clean_email(self):
		email = self.cleaned_data['email'] 
		try: 
			User.objects.get(email=email) 
		except ObjectDoesNotExist: 
			return email 
		raise forms.ValidationError('That e-mail address is already in use.')
		
	def clean(self):
		if self.cleaned_data.has_key('country'):
			if self.cleaned_data['country'] == 'US' and self.cleaned_data['state'] == 'XX':
				raise forms.ValidationError('US residents must specify a state.') 
			else:
				return self.cleaned_data



class UpdateRegistrationForm(forms.Form): 
	#user_pk = forms.IntegerField(widget=forms.HiddenInput(),label='')
	email = forms.EmailField(label='E-mail address') 
	username = forms.CharField(required=True,label='Display name', max_length=30)
	street_address = forms.CharField(required=False)
	city = forms.CharField()
	state = forms.ChoiceField(required=True,choices=STATE_CHOICES)
	country = forms.ChoiceField(required=True,choices=COUNTRY_CHOICES)
	zip = forms.CharField(label="Zip code", max_length=5,required=False)
	url = forms.URLField(label="Your web site", max_length=200,required=False)
	
	def clean_username(self): 
		username = self.cleaned_data['username'] 
		try: 
			#currentUser = User.objects.get(id=self.cleaned_data['user_pk'])
			currentUser = self.data['user']
			userQuery = User.objects.get(username=username) 
			if (currentUser == userQuery):
				return username
			else:
				raise forms.ValidationError('That display name is already taken.')
		except ObjectDoesNotExist: 
			return username 
		raise forms.ValidationError('That display name is already taken.') 
	
	def clean_email(self):

		
		email = self.cleaned_data['email'] 
		try: 
			#currentUser = User.objects.get(id=self.cleaned_data['user_pk'])
			currentUser = self.data['user']
			userQuery = User.objects.get(email=email) 
			if (currentUser == userQuery):
				return email
			else:
				raise forms.ValidationError('That e-mail address is already in use.')
		except ObjectDoesNotExist: 
			return email 
		raise forms.ValidationError('That e-mail address is already in use.')
	
	
	def clean(self):
		if self.cleaned_data.has_key('country'):
			if self.cleaned_data['country'] == 'US' and self.cleaned_data.has_key('state'):
				if self.cleaned_data['state'] == 'XX':
					raise forms.ValidationError('US residents must specify a state.') 
				else:
					return self.cleaned_data	
			else:
				return self.cleaned_data
				


				
class loginWithEmailForm(forms.Form):
	email = forms.EmailField(label='Email address') 
	password = forms.CharField( label='Password', widget=forms.PasswordInput()) 
	
	def clean_email(self):
		email = self.cleaned_data['email'] 
		try: 
			user = User.objects.get(email=email) 
			if user:
				return email
			else: 
				raise forms.ValidationError('That email address is not known.')
		except ObjectDoesNotExist: 
			raise forms.ValidationError('That e-mail address is not known.')
		
	# def clean_password(self):
	# 		pass
		
	def clean(self):
		from django.contrib.auth import login, authenticate, logout
		if self.cleaned_data.has_key('email'):
			try:
				tempUser = User.objects.get(email=self.cleaned_data['email'])  
				user = authenticate(username=tempUser.username, password=self.cleaned_data['password'])
				if user == None: 
					raise forms.ValidationError('That e-mail address and password combination is not valid')
				else:
					return self.cleaned_data
			except ObjectDoesNotExist:
				raise forms.ValidationError('That e-mail address and password combination is not valid')
		else:
			raise forms.ValidationError('That e-mail address is not known.')
			