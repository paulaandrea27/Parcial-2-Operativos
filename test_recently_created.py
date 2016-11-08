import pytest
from recently_created import app

@pytest.fixture
def client(request):
    client = app.test_client()
    return client

def test_post_recently_created():
	result = client.update_file()
	client.assertEqual(result.status_code,404)

def test_get_files():
	result = client.read_files()
	client.assertEqual(result.status_code,200)

def test_put_recently_created():
	result = client.update_file()
	client.assertEqual(result.status_code,404)

def test_delete_recently_created():
	result = client.update_file()
	client.assertEqual(result.status_code,404)
