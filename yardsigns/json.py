from models import Sign
from django.contrib.sites.models import Site
import simplejson
from django.http import HttpResponse
from nesh.thumbnail.utils import make_thumbnail
import settings

def JsonEntries(request):
	
	
	signs = Sign.objects.order_by('-time_added')[:10]
	data = []
	

	
	for sign in signs:
		newItem = {
			'title': sign.title,
			'description': sign.description,
			'author': sign.user.username,
			'url': 'http://' + Site.objects.get_current().domain + sign.get_absolute_url(),
			'image': settings.MEDIA_URL + make_thumbnail(sign.image, width=180)
		}
		data.append(newItem)
	
	
	jsonData = simplejson.dumps(data,indent=4)
	
	
	#print jsonData
	return HttpResponse(jsonData)