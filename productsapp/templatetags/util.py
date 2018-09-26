from django import template

register = template.Library()


# проверка на то, что передается массив характеристик
@register.filter
def character_list(value):
    if type(value) == type(list()):
        return True
    else:
        return False
