from django import template
from melaoapp.models import Student

register = template.Library()

@register.simple_tag(takes_context=True)
def get_student(context):
    request = context['request']
    if request.user.is_authenticated:
        try:
            return Student.objects.get(user=request.user)
        except Student.DoesNotExist:
            return None
    return None