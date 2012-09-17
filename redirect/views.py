# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.template.response import TemplateResponse
from redirect.models import Url
from django.views.decorators.cache import cache_control

@cache_page(60 * 900)
def get_short(request, short):
    try: 
        found = Url.objects.get(short=short)
        return HttpResponseRedirect(found.url)
    except Exception:
        return HttpResponseRedirect("/new")

def new_short(request):
    return HttpResponse("Short not found in system", content_type="text/plain")

@cache_control(must_revalidate=True, max_age=60, proxy_revalidate=True)
def recent(request, limit=30):
    try:
        return TemplateResponse(request, 'recent.html', {'recent_url': Url.objects.all().order_by('-timestamp')[:limit]})
    except Exception:
        return HttpResponse("shit is broken", content_type="text/plain")
