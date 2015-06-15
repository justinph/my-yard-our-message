from django.conf.urls.defaults import *
from myom2.views import *
from myom2.yardsigns.views import *  
from myom2.account.views import *  
import os.path, sys

from myom2.yardsigns.feeds import *
from myom2.yardsigns.json import *

feeds = {
    'latest': LatestEntries,
}


urlpatterns = patterns('',
	(r'^$', main_page),  
	(r'^submit/$', add_sign),
	(r'^submit/thanks/$', sign_thanks),
	
	(r'^signs/$', view_scroll),
	(r'^signs/(\d+)/$', view_scroll),
	
	(r'^signs/thumbs/$', view_thumbs),
	(r'^signs/thumbs/(\d+)/$', view_thumbs),
	#single sign
	(r'^sign/(\d+)/$', view_sign),
	(r'^sign/(\d+)/embed/$', view_sign_embed),
	
	
	(r'^logout/$', logout_page),
	(r'^account/logout/$', logout_page),
	
	(r'^login/$', register_page),
	(r'^account/register/$', register_page),
	(r'^account/$', manage_account),
	
	(r'^account/delete_sign/(\d+)/$', delete_sign),
	
	
	(r'^account/update/$', update_account),
	(r'^account/password_change/$', 'django.contrib.auth.views.password_change', {'template_name': 'account/password_change.html'}),
	(r'^account/password_change/done/$', 'django.contrib.auth.views.password_change_done', {'template_name': 'account/password_change_done.html'}),
	
	(r'^account/password_reset/$', 'django.contrib.auth.views.password_reset', {'template_name': 'account/password_reset.html','email_template_name':'account/password_email.html'}),
	(r'^account/password_reset/done/$', 'django.contrib.auth.views.password_reset_done', {'template_name': 'account/password_reset_done.html'}),
	
	
	(r'^feeds/(?P<url>.*)/$','django.contrib.syndication.views.feed', {'feed_dict': feeds}),
	
	(r'^json/$', JsonEntries),
	
	
	(r'^admin/', include('django.contrib.admin.urls')),
	
	

	
	#hack for development, serves static files as site_media, http://www.djangoproject.com/documentation/static_files/
	(r'^files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(__file__), 'files'), 	'show_indexes': True}),
	
	
	#comments
	#(r'^comments/', include('django.contrib.comments.urls.comments')),
	

)
