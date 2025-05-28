from django import template

register = template.Library()


@register.filter
def concat_lists(list1, list2):
    return list(list1) + list(list2)
