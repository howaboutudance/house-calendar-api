import pytest
from guestbook import api

def test_helloworld():
  assert sample.helloworld() == "Hello World"

def test_helloworld_name():
  assert sample.helloworld(name="Flargen") == "Hello Flargen"