import pytest
from django.urls import reverse, resolve

pytestmark = pytest.mark.django_db


def test_about():
    assert reverse("main:about") == "/about/"
    assert resolve("/about/").view_name == "main:about"
