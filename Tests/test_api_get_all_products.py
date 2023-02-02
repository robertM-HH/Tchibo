import requests
import json

class TestGetAllProducts:
    """
    This class contains the method `test_get_all_products` to test the API call to get all products.
    """
    def __init__(self):
        """
        Initializes the URL endpoint for the API call.
        """
        self.url = "https://api.predic8.de:443/shop/products/"    
    # Test to get all products   
    def test_get_all_products(self):
        """
        This method makes an API call to get all products and checks if the response status code is 200.
        """
        response = requests.get(self.url)
        assert response.status_code == 200

if __name__ == '__main__':
    getAllProducts = TestGetAllProducts()
    getAllProducts.test_get_all_products()