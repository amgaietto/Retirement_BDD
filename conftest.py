import pytest
from retirement_class import *

@pytest.fixture(scope="class")
def setup():
    test1 = Retiree()
    return test1
