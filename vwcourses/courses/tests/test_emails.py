from django.test import TestCase
from django.test.client import Client
from django.core import mail
from django.conf import settings
from django.core.urlresolvers import reverse
from vwcourses.courses.models import Course

class ContactCourseTestCase(TestCase):

  def setUp(self):
    self.course = Course.objects.create(name='Django', slug='django')

  def tearDown(self):
      self.course.delete()

  def test_contact_form_error(self):
    data = {'name': 'Fulano de tal', 'email': '', 'message': 'Mensagem de contato'}
    client = Client()
    path = reverse('courses:details', args=[self.course.slug])
    response = client.post(path, data)
    self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')

  def test_contact_form_success(self):
    data = {'name': 'Fulano de tal', 'email': 'fulano@gmail.com', 'message': 'Mensagem de contato'}
    client = Client()
    path = reverse('courses:details', args=[self.course.slug])
    response = client.post(path, data)
    self.assertEqual(len(mail.outbox), 1)
    self.assertEqual(mail.outbox[0].to, [settings.CONTACT_EMAIL])
    self.assertEqual(mail.outbox[0].subject, "[%s] Contato" % self.course.name)
    self.assertEqual(mail.outbox[0].from_email, settings.DEFAULT_FROM_EMAIL)
