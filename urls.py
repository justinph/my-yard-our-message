from django.conf.urls.defaults import *
from myom2.views import *
from myom2.yardsigns.views import *


urlpatterns = patterns('',
	(r'^$', main_page),
    
	
	(r'^submit/$', add_sign),
	(r'^submit/thanks/$', sign_thanks),
	(r'^view/$', view_signs),
	
	#(r'^accounts/', include('registration.urls')),
	
	(r'^login/$', 'django.contrib.auth.views.login'),
	
	
	#hack for development, serves static files as site_media, http://www.djangoproject.com/documentation/static_files/
	(r'^files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/justinph/Files/Misc/myom2/files', 	'show_indexes': True}),
	
	
	(r'^admin/', include('django.contrib.admin.urls')),

)
