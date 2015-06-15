from models import Sign, Tag
from django import newforms as forms
from django.newforms import form_for_model
from django.newforms import ModelForm


#SignForm = form_for_model(Sign)

# Create the form class.
class SignForm(ModelForm):
	
	class Meta:
		model = Sign
		
		
	def clean_sign_file(self):
		#print "cleaned data:"
		#print self.cleaned_data.get('sign_file','').content
		#self.filename = filename 
		#self.content = content
		from PIL import Image
		from cStringIO import StringIO
		#print "trying to clean"
		# code jacked from newforms, using to verify image just as they do there
		# but here validating the file size
		try:
			trial_image = Image.open(StringIO(self.cleaned_data.get('sign_file','').content))
			trial_image.load()
			trial_image = Image.open(StringIO(self.cleaned_data.get('sign_file','').content))
			trial_image.verify()
			mySize = trial_image.size
		except Exception: # Python Imaging Library doesn't recognize it as an image
			raise forms.ValidationError('Uploaded file not appear to be a valid JPEG image.')
		
		if mySize:
			if mySize != (4200, 2800):
				raise forms.ValidationError('Uploaded file does not appear to have the proper dimensions.')
	
		return self.cleaned_data.get('sign_file','')
		

class RegistrationForm(forms.Form): 
	username = forms.CharField(label='Username', max_length=30) 
	email = forms.EmailField(label='Email') 
	password1 = forms.CharField( label='Password', widget=forms.PasswordInput() ) 
	password2 = forms.CharField( label='Password (Again)', widget=forms.PasswordInput() ) 
			

	
TagForm = form_for_model(Tag)