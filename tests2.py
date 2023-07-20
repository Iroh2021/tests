import requests
import unittest

url = 'https://cloud-api.yandex.net/v1/disk/resources'

class TestYandexDiskAPI(unittest.TestCase):
    
    def setUp(self):
        self.token = 'your_token_here'
        self.headers = {'Authorization': f'OAuth {self.token}'}
        self.folder_name = 'Test Folder'
        self.folder_path = f'/test/{self.folder_name}/'
        
    def test_create_folder_success(self):
        params = {'path': self.folder_path}
        response = requests.put(url, headers=self.headers, params=params)
        
        self.assertEqual(response.status_code, 201) 
        self.assertTrue(response.json()['href'])

        params = {'path': '/test/'}
        response = requests.get(url, headers=self.headers, params=params)
        
        self.assertEqual(response.status_code, 200) 
        self.assertIn(self.folder_name, [item['name'] for item in response.json()['_embedded']['items']])
        
    def test_create_folder_already_exists(self):
        params = {'path': self.folder_path}
        response = requests.put(url, headers=self.headers, params=params)
        
        self.assertEqual(response.status_code, 409)

if __name__ == '__tests2__':
    unittest.main()