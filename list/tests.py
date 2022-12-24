from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from list.models import Item

from list.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_return_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEquals(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'Nowy element listy'

        response = home_page(request)
        self.assertIn('Nowy element listy', response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'new_item_text': 'Nowy element listy'}
        )
        self.assertEqual(response.content.decode(), expected_html)


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'Absolutnie pierwszy element listy'
        first_item.save()

        secound_item = Item()
        secound_item.text = 'Drugi element'
        secound_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        secound_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'Absolutnie pierwszy element listy')
        self.assertEqual(secound_saved_item.text, 'Drugi element')

