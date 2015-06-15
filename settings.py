# Django settings for myom project.
import os.path 


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('justin heideman', 'justin.heideman@walkerart.org'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = ''         # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/Users/justinph/Sites/myom_submitting/myom_static2'

#FILE_UPLOAD_MAX_MEMORY_SIZE = 51200

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://www.myyardourmessage.com/files/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = 'http://www.myyardourmessage.com/files/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'cu455m3423455641234duj(dcttfzk*3434323498723489573343#(((*#*(__))))@$(*&@#mk4@xe'


#caching
#CACHE_BACKEND = 'memcached://127.0.0.1:3243/'
#CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
	'django.middleware.http.SetRemoteAddrFromForwardedFor',
	'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
	#'django.middleware.cache.CacheMiddleware',
	'django.middleware.common.CommonMiddleware',
)

ROOT_URLCONF = 'myom2.urls'

TEMPLATE_DIRS = (
	os.path.join(os.path.dirname(__file__), 'templates'), 
	
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
	'django.contrib.admin',
	'django.contrib.flatpages',
	'django.contrib.humanize',
	#'django.contrib.comments',
	'nesh.thumbnail',
	'myom2.yardsigns',
	'myom2.account',
)
AUTHENTICATION_BACKENDS = (
    'myom2.email-auth.EmailBackend',
	'django.contrib.auth.backends.ModelBackend',
 )


# see  http://www.djangobook.com/en/1.0/chapter12/
AUTH_PROFILE_MODULE = "account.myomprofile"

#for account stuff
LOGIN_URL = '/account/register/'
LOGIN_REDIRECT_URL = '/account/'



# activation days for new users 
#ACCOUNT_ACTIVATION_DAYS=7

# settings for email, use only in testing
# DEFAULT_FROM_EMAIL = 'help@myyardourmessage.com'
# EMAIL_HOST = 'smtp.webfaction.com'
# EMAIL_HOST_USER = "wac_help"
# EMAIL_HOST_PASSWORD = "4J9hgTwGR7Q)9sC"  #fill in with a password to send mail
# EMAIL_PORT = 25
#EMAIL_USE_TLS = True
