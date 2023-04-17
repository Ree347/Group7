import unittest
import addtocart

def test_cart_page_title(self):
    response = self.client.get(reverse('cart'))
    self.assertContains(response, '<title>Cart</title>')
