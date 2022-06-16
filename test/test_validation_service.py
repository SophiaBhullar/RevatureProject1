from service.validation_service import *
import pytest

@pytest.mark.parametrize("test_name, expected", (
    ("A", False), (" ", False), (".....",False),("1", True),("4", True),("gusgwdgiwgdgugffugfygfu", False),
    ("         egfcuyqgdwywgujgu", False),("0", False),("dadfsf ffff",False)
))
def test_validate_emp_id(test_name, expected):
    assert validate_emp_id(test_name) == expected


@pytest.mark.parametrize("test_name, expected", (
    ("A", True), (" ", False), (".....",False),("Sophia", True),("Tom", True),("gusgwdgiwgdgugffugfygfu", True),
    ("         egfcuyqgdwywgujgu", False),("0", False),("dadfsf ffff",True),("fdjyhgt      ",False)
))
def test_validate_description(test_name, expected):
    assert validate_description(test_name) == expected


@pytest.mark.parametrize("test_name, expected", (
    ("$455", True), (" ", False), (".....",False),("Sophia", False),("Tom", False),("gusgwdgiwgdgugffugfygfu", False),
    ("         egfcuyqgdwywgujgu", False),("$44625", False),("dadfsf ffff",False), ("2000", False), ("0", False), ("$10", True)
))
def test_validate_amount(test_name, expected):
    assert validate_amount(test_name) == expected



@pytest.mark.parametrize("test_name, expected", (
     ("A", False), (" ", False), (".....",False),("Pending", True),("Declined", True),("Approved", True),
    ("         egfcuyqgdwywgujgu", False),("0", False),("dadfsf ffff",False)
))
def test_validate_status(test_name, expected):
    assert validate_status(test_name) == expected


@pytest.mark.parametrize("test_name, expected", (
    ("A", True), (" ", False), (".....",False),("Sophia", True),("Tom", True),("gusgwdgiwgdgugffugfygfu", True),
    ("         egfcuyqgdwywgujgu", False),("0", False),("dadfsf ffff",True), ("fchfhj      ", False)
))
def test_validate_comments(test_name, expected):
    assert validate_comments(test_name) == expected


@pytest.mark.parametrize("test_name, expected", (
     ("A", False), (" ", False), (".....",False),("Employee", True),("Manager", True),("Approved", False),
    ("         egfcuyqgdwywgujgu", False),("0", False),("dadfsf ffff",False)
))
def test_validate_designation(test_name, expected):
    assert validate_designation(test_name) == expected


@pytest.mark.parametrize("test_name, expected", (
    ("A", False), (" ", False), (".....",False),("Sophia", True),("Tom", True),("gusgwdgiwgdgugffugfygfu", False),
    ("         egfcuyqgdwywgujgu", False),("44625", False),("dadfsf ffff",False)
))
def test_validate_emp_name(test_name, expected):
    assert validate_emp_name(test_name) == expected



@pytest.mark.parametrize("test_name, expected", (
   ("ABCD", True), (" ", False),("Sophia1234", True),("Tom456", True),("gusgwdgiwgdgugffugfygfu", False),
    ("         egfcuyqgdwywgujgu", False),("44625", True),("dadfsf ffff",False)
))
def test_validate_emp_pass(test_name, expected):
    assert validate_emp_pass(test_name) == expected