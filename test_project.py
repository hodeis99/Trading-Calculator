import project
import pytest


def test_commission_questions():
    with pytest.raises(ValueError):
        project.commission_questions("By")
    with pytest.raises(ValueError):
        project.commission_questions("")


def test_commission():
    assert project.commission(10, 100, 0.2) == 2
    assert project.commission(75.67, 0.0035, 0.4) == 0.00105938
    assert project.commission(0.86, 96, 0.3) == 0.24768


def test_questions():
    with pytest.raises(ValueError):
        project.questions("   ")
    with pytest.raises(ValueError):
        project.questions("...")


def test_how_much():
    with pytest.raises(ValueError):
        project.how_much([500, 850], "Hello")
    with pytest.raises(ValueError):
        project.how_much([0.987, 896], "buuy")


def test_convert_number():
    assert project.convert_number(287.0) == 287
    assert project.convert_number(0.5999) == "0.60"
    assert project.convert_number(96.87) == "96.87"