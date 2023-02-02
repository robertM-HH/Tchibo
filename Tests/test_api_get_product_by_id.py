import requests
import json

class TestGetProductById:
    """
    This class contains the method `test_get_product_by_id` to test the API call to get a product by its ID.
    """
    def __init__(self):
        """
        Initializes the URL endpoint for the API call.
        """
        self.url = "https://api.predic8.de:443/shop/products/"    
    # Test to get a product by id   
    def test_get_product_by_id(self, id):
        """
        This method makes an API call to get a product by its ID and checks if the response status code is 200.
        :param id: ID of the product to retrieve.
        """
        response = requests.get(self.url + str(id))
        assert response.status_code == 200

if __name__ == '__main__':
    getProductById = TestGetProductById()
    getProductById.test_get_product_by_id(15)