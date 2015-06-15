from django.db import models
from nesh.thumbnail.field import ImageWithThumbnailField






#class User(models.Model):
	

from django.contrib.auth.models import User
class Sign(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	image = ImageWithThumbnailField(upload_to="signs")
	accept_terms = models.BooleanField()
	time_added = models.DateTimeField(auto_now_add=True)
	submitter_ip = models.IPAddressField(default='0.0.0.0')
	
	def __str__(self):  #defines what we normally return, should always be a string
		return self.name	
	
	class Admin: 
		list_display = ('title', 'time_added', 'user',)
		list_filter = ('title', 'time_added',)
		ordering = ('-time_added',)
		search_fields = ('sign_title',)
		
		
	class Meta:
		ordering = ['time_added']
		
		
	
	
class Tag(models.Model): 
	name = models.CharField(max_length=64, unique=True) 
	signs = models.ManyToManyField(Sign) 
	
	
	class Admin: 
		pass