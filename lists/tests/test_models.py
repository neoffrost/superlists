from django.test import TestCase
from django.core.exceptions import ValidationError
from lists.models import Item, List

class ListAndItemModelsTest(TestCase):
	def test_cannot_save_empty_list_items(self):
		list_ = List.objects.create()
		item = Item(list=list_, text='')
		with self.assertRaises(ValidationError):
			item.save()
			item.full_clean()

	def test_get_absolute_url(self):
		list_ = List.objects.create()
		self.assertEqual(list_.get_absolute_url(), '/lists/%d/' % (list_.id,))