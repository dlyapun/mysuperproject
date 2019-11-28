from django.test import TestCase
from myAPP.models import Pizza
class YourTestClass(TestCase): # from django.test import TestCase
    def setUp(self):
        pass # Установки запускаются перед каждым тестом
    @classmethod
    def setUpTestData(cls):
        Pizza.objects.create(name='My pizza', price=100) # id 1
        Pizza.objects.create(name='My pizza 2', price=200) # id 2
    def test_basic_addition(self):
        self.assertEqual(1 + 1, 2)
    def test_something_that_will_pass(self):
        self.assertFalse(False)
        pizza = Pizza.objects.get(id=1)
        self.assertEquals(pizza.name, 'My pizza')

    def test_pizzas_page(self):
        response = self.client.post('/pizzas/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My pizza, цена: 100.00')
        self.assertTrue('pizzas' in response.context)
        self.assertTrue(len(response.context['pizzas']) == 2)
        self.assertEqual(response.context['pizzas'][1].price, 200)
        
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h1>Bootstrap starter template</h1>')
        
    def test_change_price_method(self):
        pizza = Pizza.objects.get(id=1)
        pizza.change_price(48)
        self.assertEquals(pizza.price, 148)