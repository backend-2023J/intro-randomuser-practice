import requests
import json

url = 'https://randomuser.me/api/'


def get_version():
    '''get requests module'''
    return requests.__version__


def get_status_code(url: str) -> int:
    '''get status code of response
    
    Args:
        url (str): api url
    
    Returns:
        str: status code of response
    '''
    response =  requests.get(url)
    return response.status_code


def get_content_type(url: str) -> str:
    '''get content type of response
    
    Args:
        url (str): api url
    
    Returns:
        str: content type of response
    '''
    response = requests.get(url)
    return response.headers['Content-Type']


def get_headers(url: str) -> dict:
    '''get headers of response
    
    Args:
        url (str): api url
    
    Returns:
        str: headers of response
    '''
    response =  requests.get(url)
    return response.headers


def get_text(url: str) -> str:
    '''get text of response
    
    Args:
        url (str): api url
    
    Returns:
        str: text of response
    '''
    response = requests.get(url)
    return (response.text)


def text_to_dict(text: str) -> dict:
    '''convert text to dict
    
    Args:
        text (str): text of response
    
    Returns:
        str: dict
    '''
    data = json.loads(get_text(url))
    return data


def get_data(url: str) -> dict:
    '''get data of response. use method json()
    
    Args:
        url (str): api url
    
    Returns:
        dict: data
    '''
    response = requests.get(url)
    data = response.json()
    return data

def get_user(url: str) -> dict:
    '''get user
    
    Args:
        url (str): api url
    
    Returns:
        dict: user
    '''
    response = requests.get(url)
    data = response.json()
    return data['results'][0]

def get_users(url: str, n: int) -> list:
    '''get user
    
    Args:
        url (str): api url
        n (int): number of users
    
    Returns:
        list: list of users
    '''
    users_data = []

    for i in range(n):
        user = get_user(url)
        users_data.append(user)

    return users_data

print(get_version())
print(get_status_code(url))
print(get_content_type(url))
print(get_headers(url), "\n")
print(get_text(url))
print(text_to_dict(get_text(url)))
print(get_data(url))
print(get_user(url))
print(get_users(url, 5))
