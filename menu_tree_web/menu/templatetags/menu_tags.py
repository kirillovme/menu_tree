from django import template
from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context: dict, menu_name: str) -> dict:
    """Кастомный тег для отрисовки древовидного меню."""
    request = context['request']
    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')

    def build_tree(items):
        tree = {}
        for item in items:
            item.url_resolved = item.get_absolute_url()
            item.is_active = (request.path == item.url_resolved)
            tree.setdefault(item.parent_id, []).append(item)
        return tree

    menu_tree = build_tree(menu_items)

    def build_menu_structure(parent_id, tree):
        if parent_id not in tree:
            return []
        branch = []
        for node in tree[parent_id]:
            children = build_menu_structure(node.id, tree)
            branch.append((node, children))
        return branch

    menu_structure = build_menu_structure(None, menu_tree)

    return {'menu_structure': menu_structure}
