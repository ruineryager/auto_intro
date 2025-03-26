import requests
import json


def test_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    for x in response:
        print(x['title'])
    # assert len(response) == 100


def test_get_posts():
    headers = {'Content-type': 'application/json; charset=UTF-8'
               }
    body = json.dumps({'title': 'foo',
                       'body': 'bar',
                       'userId': 1
                       })
    response = requests.post('https://jsonplaceholder.typicode.com/posts/',
                             data=body,
                             headers=headers
                             )
    print(response.json())
    print(response.status_code)
    # assert len(response) == 10
    #

def test_put_posts():
    headers = {'Content-type': 'application/json; charset=UTF-8'
               }
    body = json.dumps({'title': 'foo',
                       'body': 'bar',
                       'userId': 1
                       })
    response = requests.put('https://jsonplaceholder.typicode.com/posts/42',
                             data=body,
                             headers=headers
                             )
    print(response.json())
    print(response.status_code)

def test_patch_posts():
    headers = {'Content-type': 'application/json; charset=UTF-8'
               }
    body = json.dumps({'title': 'foo1',
                       'userId': 1
                       })
    response = requests.patch('https://jsonplaceholder.typicode.com/posts/42',
                             data=body,
                             headers=headers
                             )
    print(response.json())
    print(response.status_code)

def test_delete_posts():
    response = requests.delete('https://jsonplaceholder.typicode.com/posts/42')
    print(response.json())
    print(response.status_code)

test_delete_posts()
