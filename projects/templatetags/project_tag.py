from django import template

register = template.Library()
    
@register.filter
def statusmessage(args):
    return "55555"







