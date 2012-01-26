from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.conf import settings
from django.views.decorators.cache import cache_page
import redis

redis_server = redis.Redis(settings.CACHE)

@cache_page(60 * 900)
def get_short(request, short):
    found_url = "http://www.google.com"
    for url in redis_server.keys('http*'):
        if redis_server.hget(url, 'short') == short:
            found_url = url
    return HttpResponseRedirect(found_url)
