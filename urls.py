from django.conf.urls.defaults import *
from myom.views import *
from myom.yardsigns.views import *

urlpatterns = patterns('',
	(r'^$', main_page),
    
	
	(r'^submit/$', add_sign),
	(r'^submit/thanks/$', sign_thanks),
	
	(r'^admin/', include('django.contrib.admin.urls')),
	#hack for development, serves static files as site_media, http://www.djangoproject.com/documentation/static_files/
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/justinph/Files/Misc/mysite/media', 	'show_indexes': True}),

)
