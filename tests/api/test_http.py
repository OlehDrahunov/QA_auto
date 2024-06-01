import pytest
import requests

@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(f'HTTP response: {r.status_code} text of message: {r.text.upper()}')

@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/revolmax')
    body = r.json()
    headers = r.headers
    #print(f'HTTP response: {r.status_code} text of message: {r.text.upper()}')
    assert r.status_code == 200 
    #print(f'Response Body: {r.json()}')
    assert body['login'] == 'revolmax'
    #print(f'Response Headers: {r.headers}') 
    assert headers["Server"] == "GitHub.com"

@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/22_gfgffdjdfdj')
    assert r.status_code == 404
