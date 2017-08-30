from django.contrib import admin

# Register your models here.
from letsgo.models import Event
#and register it 
#admin.site.register(Event)

class EventAdmin(admin.ModelAdmin):
	model = Event
	list_display = ('name', 'host', 'time', 'date', 'blurb','description', 'categories', 'location', 'price')
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Event, EventAdmin)

