# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.conf import settings
from django.views.decorators.cache import cache_page
from redirect.models import Url

@cache_page(60 * 900)
def get_short(request, short):
    try: 
        found = Url.objects.get(short=short)
        return HttpResponseRedirect(found.url)
    except Exception:
        return HttpResponseRedirect("http://google.com")
