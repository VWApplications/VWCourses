from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

class HomeViewTest(TestCase):

  def setUp(self):
    """
      Esse é o método que será rodado entes de rodar qualquer outro método
      Ele irá inicializar a variável client e pegar o HttpResponse da URL da view home
    """
    client = Client()
    self.response = client.get(reverse('core:home'))

  def test_home_status_code(self):
    """
      Esse teste irá testar se o codigo de status é igual a 200 OK para renderização de templates, no caso o template home.html
    """
    self.assertEqual(self.response.status_code, 200)

  def test_home_template_used(self):
    """
      Esse teste irá verificar se os templates estão sendo usados na requisição da view home, home.html, base.html, navbar.html e footer.html
    """
    self.assertTemplateUsed(self.response, 'core/home.html')
    self.assertTemplateUsed(self.response, 'core/base.html')
    self.assertTemplateUsed(self.response, 'core/footer.html')
    self.assertTemplateUsed(self.response, 'core/navbar.html')
