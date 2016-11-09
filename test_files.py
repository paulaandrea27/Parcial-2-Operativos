import pytest
import json
import unittest
import tempfile
import os
from files import app

class FlaskTestCase(unittest.TestCase):

	def test_create_file(self):
		client = app.test_client(self)
		result = client.post('/v1.0/files',data=json.dumps(dict(filename='new file',content='content')),follow_redirects=True)
		self.assertEqual(result.status_code,201)

	def test_read_files(self):
		client = app.test_client(self)
		result = client.get('/v1.0/files',follow_redirects=True)
		self.assertEqual(result.status_code,200)

	def test_delete_files(self):
		client = app.test_client(self)
		result = client.delete('/v1.0/files',follow_redirects=True)
		self.assertEqual(result.status_code,200)

if __name__ == '__main__':
    unittest.main()