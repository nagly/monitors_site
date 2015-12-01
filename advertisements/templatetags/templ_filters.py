from django import template

register = template.Library()

@register.filter
def TimeDifference(value):
    from django.utils import timezone

    delta = value - timezone.now()
    if delta.days >= 2:
        return '%s days' %delta.days
    if delta.days >= 1:
        return '1 day'
    elif delta.seconds > 7200:
        return str(delta.seconds / 3600 ) + ' hours'
    elif delta.seconds > 3600:
        return '1 hour'
    else:
        return str(delta.seconds/60) + ' minutes'
    return defaultfilters.date(value)

@register.filter
def multiply(value, arg):
    return value*arg