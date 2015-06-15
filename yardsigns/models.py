from django.db import models
from nesh.thumbnail.field import ImageWithThumbnailField
from django.contrib.auth.models import User




class Sign(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	image = ImageWithThumbnailField(upload_to="signs/%j")
	accept_terms = models.BooleanField(blank=False,core=True)
	time_added = models.DateTimeField(auto_now_add=True)
	submitter_ip = models.IPAddressField(default='0.0.0.0')
	approved = models.BooleanField(blank=True,default=True)
	
	def __str__(self):  #defines what we normally return, should always be a string
		return self.title	
	
	def get_absolute_url(self):
		return "/sign/%i/" % self.id
	
	class Admin: 
		list_display = ('title', 'time_added', 'user','approved',)
		list_filter = ('title', 'time_added','approved',)
		ordering = ('-time_added',)
		search_fields = ('sign_title',)
		
		
	class Meta:
		ordering = ['time_added']
		
		
