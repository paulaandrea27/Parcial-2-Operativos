import pytest
from recently_created import app

@pytest.fixture
def client(request):
    client = app.test_client()
    return client

def test_post_recently_created(client):
	result = client.post("/v1.0/files/recently_created")
	assertEqual(result.status_code,404)

def test_get_files(client):
	result = client.get("/v1.0/files/recently_created")
	assertEqual(result.status_code,200)

def test_put_recently_created(client):
	result = client.put("/v1.0/files/recently_created")
	assertEqual(result.status_code,404)

def test_delete_recently_created(client):
	result = client.delete("/v1.0/files/recently_created")
	assertEqual(result.status_code,404)
