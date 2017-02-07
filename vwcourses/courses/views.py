from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import enrollment_required
from .models import Course, Enrollment, Announcement, Lesson, Material
from .forms import ContactCourseForm, CommentForm


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


@login_required
def enrollment(request, course_slug):
  course = get_object_or_404(Course, slug=course_slug)
  enrollment, is_created = Enrollment.objects.get_or_create(user=request.user, course=course)
  if is_created:
    enrollment.active()
    messages.success(request, "Você foi inscrito no curso com sucesso!")
  else:
    messages.info(request, "Você já está inscrito no curso!")
  return redirect('accounts:profile')


@login_required
def cancel_enrollment(request, course_slug):
  template = 'courses/cancel_enrollment.html'
  course = get_object_or_404(Course, slug=course_slug)
  enrollment = get_object_or_404(Enrollment, user=request.user, course=course)
  if request.method == 'POST':
    enrollment.delete()
    messages.success(request, 'Sua inscrição foi cancelada com sucesso')
    return redirect('accounts:profile')
  context = {'enrollment': enrollment, 'course': course}
  return render(request, template, context)


@login_required
@enrollment_required
def announcements(request, course_slug):
  template = 'courses/announcements.html'
  course = request.course
  context = {
    'course': course,
    'announcements': course.announcements.all()
  }
  return render(request, template, context)


@login_required
@enrollment_required
def show_announcement(request, course_slug, announcement_id):
  template = 'courses/show_announcements.html'
  course = request.course
  announcement = get_object_or_404(course.announcements.all(), pk=announcement_id)
  form = CommentForm(request.POST or None)
  if form.is_valid():
    comment = form.save(commit=False)
    comment.user = request.user
    comment.announcement = announcement
    comment.save()
    form = CommentForm()
    messages.success(request, 'Seu comentario foi enviando com sucesso')
  context = {
    'course': course,
    'announcement': announcement,
    'form': form,
  }
  return render(request, template, context)


@login_required
@enrollment_required
def lessons(request, course_slug):
  template = 'courses/lessons.html'
  course = request.course
  lessons = course.release_lessons()
  if request.user.is_staff:
    lessons = course.lessons.all()
  context = {'course': course, 'lessons': lessons}
  return render(request, template, context)


@login_required
@enrollment_required
def lesson(request, course_slug, lesson_id):
  template = 'courses/lesson.html'
  course = request.course
  lesson = get_object_or_404(Lesson, pk=lesson_id, course=course)
  if not request.user.is_staff and not lesson.is_available():
    messages.error(request, "Está aula não está disponível")
    return redirect('courses:lessons', slug=course.slug)
  context = {'course': course, 'lesson': lesson}
  return render(request, template, context)


@login_required
@enrollment_required
def material(request, course_slug, material_id):
  template = 'courses/material.html'
  course = request.course
  material = get_object_or_404(Material, pk=material_id, lesson__course=course)
  lesson = material.lesson
  if not request.user.is_staff and not lesson.is_available():
    messages.error(request, "Este material não está disponível")
    return redirect('courses:lesson', slug=course.slug, pk=lesson.id)
  if not material.is_embedded():
    return redirect(material.file.url)
  context = {'course': course, 'lesson': lesson, 'material': material}
  return render(request, template, context)

@login_required
@enrollment_required
def information(request, course_slug):
  template = 'courses/information.html'
  course = request.course
  context = {'course': course}
  return render(request, template, context)
