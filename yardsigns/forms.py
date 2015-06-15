from models import Sign
from django import newforms as forms


# Create the form class.
class SignForm(forms.Form):
	
	title = forms.CharField(required=True)
	description = forms.CharField(widget=forms.Textarea(),help_text="This will show up next to your sign.",required=False)
	image = forms.FileField(required=True,help_text="Maximum file size 10 megabytes.")
	accept_terms = forms.BooleanField(required=True,help_text="You accept the terms of agreement (below).")
		
		
	def clean_image(self):
		'''
		code jacked from newforms, using to verify image just as they do there
		but here validating the file size
		'''
		from PIL import Image
		from cStringIO import StringIO

		try:
			trial_image = Image.open(StringIO(self.cleaned_data.get('image','').content))
			trial_image.load()
			trial_image = Image.open(StringIO(self.cleaned_data.get('image','').content))
			trial_image.verify()
			mySize = trial_image.size
		except Exception: # Python Imaging Library doesn't recognize it as an image
			raise forms.ValidationError('Uploaded file not appear to be a valid JPEG image.')
		
		if mySize:
			if mySize != (4200, 2800):
				raise forms.ValidationError('Uploaded file does not appear to have the proper dimensions. Please make sure you sign is 4200px wide and 2800px tall.')
	
		return self.cleaned_data.get('image','')
	
	def clean_accept_terms(self):
		if self.cleaned_data.get('accept_terms') == False:
			raise forms.ValidationError("You must accept the terms of service to submit your sign.")
		else: 
			return self.cleaned_data.get('accept_terms')



class DeleteSign(forms.Form):
	confirm = forms.CharField(required=True,help_text="Please type 'DELETE' in all caps to confirm your choice to delete this sign.",label="Confirm delete")
	
	def clean_confirm(self):
		if self.cleaned_data['confirm'] != 'DELETE':
			print 'invalid'
			raise forms.ValidationError("You must type 'DELETE' to confirm the deletion of the sign.")
		else:
			print "seems ok"
			return self.cleaned_data['confirm']
			