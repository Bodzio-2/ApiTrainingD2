import requests

BASE_URL = 'https://fakestoreapi.com'

query_params = {
    "limit": 3
}

new_product = {
"title": 'test product',
"price": 13.5,
"description": 'lorem ipsum set',
"image": 'https://i.pravatar.cc',
"category": 'electronic'

}

response = requests.post(f"{BASE_URL}/products", json=new_product)
print(response.json())

#response = requests.get(f"{BASE_URL}/products", params=query_params)
#response = requests.get(f"{BASE_URL}/products/18")
#print(response.json())
#print(response.status_code)