from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import setari

def index(request):
    context={
            'FB_APP_ID':setari.FB_APP_ID,
            'FB_APP_SECRET_KEY':setari.FB_APP_SECRET_KEY,
            }
    return render_to_response('index.html', context,
            context_instance=RequestContext(request))

