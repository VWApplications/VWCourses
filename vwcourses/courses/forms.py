from django import forms
from django.conf import settings
from vwcourses.core.mail import send_email_template

class ContactCourseForm(forms.Form):
  name = forms.CharField(label='Nome', max_length=100)
  email = forms.EmailField(label='Email')
  message = forms.CharField(label='Mensagem', widget=forms.Textarea)

  def send_message(self, course):
    template = 'courses/contact_email.html'
    subject = '[%s] Contato' % course
    context = {
      'name': self.cleaned_data['name'],
      'email': self.cleaned_data['email'],
      'message': self.cleaned_data['message']
    }
    send_email_template(subject, template, context, [settings.CONTACT_EMAIL])
