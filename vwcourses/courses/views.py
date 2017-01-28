from django.shortcuts import render, get_object_or_404
from .models import Course
from .forms import ContactCourse


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
  if request.method == 'POST':
    form = ContactCourse(request.POST)
    if form.is_valid():
      print("O formulario está valido")
      print(form.cleaned_data['message'])
      form = ContactCourse()
  else:
    form = ContactCourse()
  context = {
    'course': course,
    'form': form,
  }
  return render(request, template, context)
