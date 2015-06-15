from models import Sign, Tag
from django import newforms as forms
from django.newforms import form_for_model
from django.newforms import ModelForm


#SignForm = form_for_model(Sign)

# Create the form class.
class SignForm(ModelForm):
	
	class Meta:
		model = Sign
		#sign_file = forms.Field(help_text=('Upload an image (max %s kilobytes)' % settings.MAX_PHOTO_UPLOAD_SIZE))
		
	def clean_sign_file(self):
		#print self.cleaned_data.get('sign_file','').content
		#self.filename = filename 
		#self.content = content
		from PIL import Image
		from cStringIO import StringIO
		
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
	
	
	
TagForm = form_for_model(Tag)