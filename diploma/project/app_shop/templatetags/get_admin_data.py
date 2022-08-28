from django import template
import datetime

from app_profile.models import Profile


register = template.Library()


@register.simple_tag
def get_admin_data():
    admin = Profile.objects.select_related('user').filter(user__is_staff=True).first()
    return admin