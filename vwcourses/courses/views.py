from django.shortcuts import render, get_object_or_404
from .models import Course
from .forms import ContactCourseForm


def index(request):
  template = 'courses/index.html'
  courses = Course.objects.all()
  context = {
    'courses': courses,
  }
  return render(request, template, context)


def details(request, course_slug):
  template = 'courses/details.html'
  course = get_object_or_404(Course, slug=course_slug)
  context = {}
  if request.method == 'POST':
    form = ContactCourseForm(request.POST)
    if form.is_valid():
      context['is_valid'] = True
      form.send_message(course)
      form = ContactCourseForm()
  else:
    form = ContactCourseForm()
  context['course'] = course
  context['form'] = form
  return render(request, template, context)
