import requests

def test_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    print(response)
    assert len(response) == 100
