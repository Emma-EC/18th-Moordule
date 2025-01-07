from django import template

register = template.Library()


@register.inclusion_tag("shared/navigator.html", takes_context=True)
def navigator(context):

    nav_items = [
        {"title": "我的頁面", "url": "", "name": "member"},  # member 的 url 為空
        {"title": "我的帳號", "url": "account", "name": "account"},
        {"title": "我的聚會", "url": "activities", "name": "activities"},
        {"title": "創建聚會", "url": "activity_form", "name": "activity_form"},
    ]
    return {"nav_items": nav_items}
