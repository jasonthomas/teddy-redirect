import os, sys
sys.path.append('/home/lithium/domains/wgeturl.com')
os.environ['DJANGO_SETTINGS_MODULE'] = 'teddy.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
