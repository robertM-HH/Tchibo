import requests
import json

class ProductsApiTests:
    
    def __init__(self):
        self.url = "https://api.predic8.de:443/shop/products/"
     
    # Test to get all products   
    def test_get_all_products(self):
        response = requests.get(self.url)
        assert response.status_code == 200
    
    # Test to create a new product
    def test_post_product(self, data):
        response = requests.post(self.url, json=data)
        assert response.status_code == 201
        new_product_name = json.loads(response.text)
        assert new_product_name["name"] == "Tomaten"

    # Test to get a specific product
    def test_get_product_by_id(self, id):
        response = requests.get(self.url + str(id))
        assert response.status_code == 200
    
    # Test to update a product
    def test_update_product(self, id, data):
        response = requests.put(self.url + str(id), json=data)
        assert response.status_code == 200
       
    # Test to delete a product     
    def test_delete_product(self, id):
        response = requests.delete(self.url + str(id))
        assert response.status_code == 200
           
        
if __name__ == '__main__':
    productsAPI_obj = ProductsApiTests()
    productsAPI_obj.test_get_all_products()
    productsAPI_obj.test_post_product({
                                "name": "Tomaten",
                                "price": 9.99,
                                "category_url": "/shop/categories/Fruits",
                                "vendor_url": "/shop/vendors/672"
                                })
    productsAPI_obj.test_get_product_by_id(16)
    productsAPI_obj.test_update_product(16,
                                {
                                "name": "Tomaten",
                                "price": 10.99
                                })
    productsAPI_obj.test_delete_product(15)