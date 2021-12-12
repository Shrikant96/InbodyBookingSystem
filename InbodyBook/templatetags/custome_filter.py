from django import template
from InbodyBook.models import Machine
register = template.Library()

def region_filter(value):
    mechine=Machine.objects.filter(region=value)
    return mechine
register.filter('region_filter',region_filter)