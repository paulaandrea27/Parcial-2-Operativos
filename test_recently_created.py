import pytest
import json
import unittest
import tempfile
import os
from files import app

class FlaskTestCase2(unittest.TestCase):

	def test_get_files(self):
		client = app.test_client(self)
		result = client.get('/v1.0/files/recently_created',follow_redirects=True)
		self.assertEqual(result.status_code,200)

if __name__ == '__main__':
    unittest.main()