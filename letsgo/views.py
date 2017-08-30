from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
# Create your views here.

from letsgo.models import Event
from django.template.defaultfilters import slugify
# Create your views here.

def eventlist(request):
    events = Event.objects.all()
    return render(request, 'eventlist.html', {
        'events': events,
    })

def eventdes(request, slug):
    event = Event.objects.get(slug=slug)
    return render(request, 'eventdes.html', {
        'event': event,
    })

def imagereq(request, photo):
    p = Event.objects.get(photo=photo)
    return render(request, 'eventlist.html', {
          'p':p,
    }) 
