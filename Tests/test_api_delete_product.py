import requests
import json

class TestDeleteProduct:
    """
    This class contains the method `test_delete_product` to test the API call to delete a product.
    """
    def __init__(self):
        """
        Initializes the URL endpoint for the API call.
        """
        self.url = "https://api.predic8.de:443/shop/products/"       
    # Test to delete a product   
    def test_delete_product(self, id):
        """
        This method makes an API call to delete a product and checks if the response status code is 200.
        :param id: ID of the product to be deleted.
        """
        response = requests.delete(self.url + str(id))
        assert response.status_code == 200

if __name__ == '__main__':
    deleteProduct = TestDeleteProduct()
    deleteProduct.test_delete_product(15)




if __name__ == '__main__':
    deleteProduct = TestDeleteProduct()
    deleteProduct.test_delete_product(15)