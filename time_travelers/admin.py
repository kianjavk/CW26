from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import TimeTraveler

class TimeTravelerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'bold_national_code','gender']
    fields = [('first_name','last_name'), 'national_code', 'gender']
    search_fields = ['national_code']
    list_filter = [ 'gender']


    def full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'

    # @admin.display(description="National Code")
    def bold_national_code(self,obj):
        return format_html(f'<strong>{obj.national_code}</strong>')

    bold_national_code.short_description = "National Code"


# @admin.display(description="National Code")
admin.site.register(TimeTraveler, TimeTravelerAdmin)