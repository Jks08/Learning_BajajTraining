import requests

def fetch(url):
    sesssion = requests.Session()
    return sesssion.get(url)