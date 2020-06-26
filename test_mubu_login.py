import json
import requests
import unittest

class TestLogin(unittest.TestCase):
    def test_get_homepage(self):
        url = 'https://mubu.com/'
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4168.2 Safari/537.36'}
        response = requests.get(url=url, headers=headers, verify=False)
        assert response.status_code == 200

    def test_get_login(self):
        url = 'https://mubu.com/api/login/submit'
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4168.2 Safari/537.36',
                   'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        data = 'phone=17612126297&password=141214&remember=true'
        response = requests.post(url=url, headers=headers, data=data, verify=False).json()
        assert response['code'] == 0

# if __name__ == "__main__":
#     unittest.main()

