import os
import site
# Add the app dir to the python path so we can import manage.
wsgidir = os.path.dirname(__file__)
site.addsitedir(os.path.abspath(os.path.join(wsgidir, '../')))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
