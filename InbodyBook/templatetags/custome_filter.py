from django import template
from InbodyBook.models import Meachines
register = template.Library()

def region_filter(value):
    mechine=Meachines.objects.filter(region=value)
    return mechine
register.filter('region_filter',region_filter)