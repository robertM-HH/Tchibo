import requests
import json

class TestPostProduct:
    """
    This class contains the method `test_post_product` to test the API call to add a new product.
    """
    def __init__(self):
        """
        Initializes the URL endpoint for the API call.
        """
        self.url = "https://api.predic8.de:443/shop/products/"
     
    # Test to get all products   
    def test_post_product(self, data):
        """
        This method makes an API call to add a new product and checks if the response status code is 201.
        It also checks if the name of the newly added product is as expected.
        :param data: Data for the new product to be added.
        """
        response = requests.post(self.url, json=data)
        assert response.status_code == 201
        new_product_name = json.loads(response.text)
        assert new_product_name["name"] == "Tomaten"

if __name__ == '__main__':
    postProduct = TestPostProduct()
    postProduct.test_post_product({
                                "name": "Tomaten",
                                "price": 9.99,
                                "category_url": "/shop/categories/Fruits",
                                "vendor_url": "/shop/vendors/672"
                                })