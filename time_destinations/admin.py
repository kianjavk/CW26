from django.contrib import admin

# Register your models here.
from .models import TimeDestination

class TimeDestinationAdmin(admin.ModelAdmin):
    list_display = ['name','origin_destination','description']
    fields = ['name',('origin','destination'),'description']


    def origin_destination(self,obj):
        return f'{obj.origin} -  {obj.destination}'





admin.site.register(TimeDestination, TimeDestinationAdmin)