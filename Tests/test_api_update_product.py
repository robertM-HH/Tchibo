import requests
import json

class TestUpdateProduct:
    """
    This class contains the method `test_update_product` to test the API call to update a product.
    """
    def __init__(self):
        """
        Initializes the URL endpoint for the API call.
        """
        self.url = "https://api.predic8.de:443/shop/products/"
     
    # Test to get all products   
    def test_update_product(self, id, data):
        """
        This method makes an API call to update a product and checks if the response status code is 200.
        :param id: ID of the product to be updated.
        :param data: Data for the product to be updated.
        """
        response = requests.put(self.url + str(id), json=data)
        assert response.status_code == 200

if __name__ == '__main__':
    updateProduct = TestUpdateProduct()
    updateProduct.test_update_product(15,
                                {
                                "name": "Tomaten",
                                "price": 10.99
                                })