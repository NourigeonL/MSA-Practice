import pytest
import unittest
from unittest import mock
from src.app import app
from fastapi.testclient import TestClient

class IntegrationTest(unittest.TestCase):
  def setUp(self) -> None:
    self.client = TestClient(app)