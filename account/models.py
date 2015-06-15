from django.db import models
from django.contrib.auth.models import User
from choices import *

class MyomProfile(models.Model):
	user = 	models.ForeignKey(User, unique=True, edit_inline=models.STACKED, num_in_admin=1,min_num_in_admin=1, max_num_in_admin=1,num_extra_on_change=0)

	street_address = models.CharField(max_length=100, blank=True )
	city = models.CharField(max_length=50,core=True)
	state = models.USStateField(max_length=2, choices=STATE_CHOICES)
	country = models.CharField(max_length=2, core=True,choices=COUNTRY_CHOICES)
	zip = models.IntegerField(max_length=5,core=False,blank=True)
	url = models.URLField(core=False,blank=True)

	def __str__(self):  #defines what we normally return, should always be a string
		return self.user.username	
		
	def get_pk(self):
		return self.data['uid']
	
