from django.template import Library
from vwcourses.courses.models import Enrollment

register = Library()

@register.assignment_tag
def load_my_courses(user):
  return Enrollment.objects.filter(user=user)


