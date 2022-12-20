
from magazinslunce.products.models import Product
from tests.products.BaseTestCase import TestCaseBase


class DetailsProductView(TestCaseBase):
    URL_PATTERN = '/products/{}/details/'
    VALID_USER_DATA = {
        'username': 'test_user',
        'email': 'test_user@magazinslunce.bg',
        'password': 'parola1234',
    }

    def test_details_product__view_when_user_is_authenticated__expect_product(self):
        self._create_user_and_login(self.VALID_USER_DATA)
        obj = Product.objects.create(
            name='Product_name',
            type='type',
            Image='img.png',
            price=3,
        )
        response = self.client.get(self.URL_PATTERN.format(obj.pk))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'].name, 'Product_name')

    def test_details_product__view_when_user_not_authenticated__expect_redirect_to_login(self):
        obj = Product.objects.create(
            name='Product_name',
            type='type',
            Image='img.png',
            price=3,
        )
        response = self.client.get(self.URL_PATTERN.format(obj.pk))

        self.assertEqual(response.url.strip('/').split('/')[1], 'login')
