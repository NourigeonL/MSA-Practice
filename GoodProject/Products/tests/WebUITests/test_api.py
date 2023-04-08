import pytest
import unittest
from fastapi.testclient import TestClient
from src.WebUI.main import app

class APITest(unittest.TestCase):
  def setUp(self) -> None:
    self.client = client = TestClient(app)

  def test_root(self):

    response = self.client.get("/")
    assert response.status_code == 200

  def test_get_all_products_endpoint(self):
    response = self.client.get("/products/")
    assert response.status_code == 200

  def test_get_all_products_return_list(self):
    response = self.client.get("/products/")
    assert isinstance(response.json() ,list)