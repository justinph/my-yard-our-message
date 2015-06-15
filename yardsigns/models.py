from django.db import models
from nesh.thumbnail.field import ImageWithThumbnailField
# make sure to use nesh from /Library/Python/2.5/site-packages/ on illest-book



class Sign(models.Model):
	name = models.CharField(max_length=40)
	email = models.EmailField()
	city = models.CharField(max_length=30)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=30)
	website = models.URLField(blank=True)
	sign_title = models.CharField(max_length=200)
	sign_description = models.TextField(blank=True)
	#sign_file = models.FileField(upload_to="signs")
	sign_file = ImageWithThumbnailField(upload_to="signs")
	accept_terms = models.BooleanField()
	time_added = models.DateTimeField(auto_now_add=True)
	submitter_ip = models.IPAddressField(default='0.0.0.0')
	
	def __str__(self):  #defines what we normally return, should always be a string
		return self.name	
	
	class Admin: 
		list_display = ('sign_title', 'time_added', 'email',)
		list_filter = ('name', 'time_added',)
		ordering = ('-time_added',)
		search_fields = ('sign_title',)
		
		
	class Meta:
		ordering = ['time_added']
		
		
	
	
class Tag(models.Model): 
	name = models.CharField(max_length=64, unique=True) 
	signs = models.ManyToManyField(Sign) 
	
	
	class Admin: 
		pass