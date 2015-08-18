from custom_menu.models import NodeModel, Menu
from django import template
from django.conf import settings


register = template.Library()


def draw_menu(context, menu_name):
    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist as e:
        if settings.TEMPLATE_DEBUG:
            raise e
        else:
            return context
    context['menu'] = menu
    context['menu_name'] = menu_name
    return context

register.inclusion_tag('custom_menu/menu.html', takes_context=True)(draw_menu)


def draw_node(context, node):
    if not isinstance(node, NodeModel):
        error_message = 'Given argument must be a NodeModel object.'
        raise template.TemplateSyntaxError(error_message)

    context['node'] = node
    request = context['request']
    if request.path.startswith(node.get_parent_url()):
        context['is_draw'] = True
    else:
        context['is_draw'] = False
    return context

register.inclusion_tag('custom_menu/node.html', takes_context=True)(draw_node)