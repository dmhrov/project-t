import unittest
import requests
import time
import subprocess
import os
import signal

class TestFlaskApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Запускаємо додаток у фоновому режимі
        cls.process = subprocess.Popen(["python", "app.py"])
        # Чекаємо, щоб додаток запустився
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        # Зупиняємо процес додатку
        cls.process.kill()

    def test_health_endpoint(self):
        response = requests.get('http://localhost:5000/api/health')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['status'], 'healthy')

if __name__ == '__main__':
    unittest.main()