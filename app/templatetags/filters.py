from django import template

register = template.Library()


@register.filter()
def to_float(value):
    if value is None:
        return

    if len(value.strip()) == 0:
        return

    return float(value)
