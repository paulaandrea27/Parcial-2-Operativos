import pytest
from files import app

@pytest.fixture
def client(request):
    client = app.test_client()
    return client

def test_create_file(client):
	result = client.post("/v1.0/files")
	assertEqual(result.status_code,201)

def test_read_files(client):
	result = client.get("/v1.0/files")
	assertEqual(result.status_code,200)

def test_update_file(client):
	result = client.put("/v1.0/files")
	assertEqual(result.status_code,404)

def test_delete_files(client):
	result = client.delete("/v1.0/files")
	assertEqual(result.status_code,200)