from pytest_bdd import scenario, given, when, then, scenarios, parsers
from _pytest.monkeypatch import MonkeyPatch
from io import StringIO
from retirement_class import Retiree
import pytest



@scenario('../features/data_entry.feature', 'Program accepts valid date entry')
def test_add():
    pass


@given("the Full Retirement Age Calculator is started")
def start():
    pass


@when('the year "1987" is entered')
def year_setup(setup, monkeypatch):
    choice = StringIO('1987\n')
    monkeypatch.setattr('sys.stdin', choice)
    setup.get_birth_year()



@then("the value is accepted")
def check_value(setup):
    assert setup.year == 1987










@scenario('../features/data_entry.feature', 'Program accepts valid month entry')
def test_month():
    pass


@given("a valid year has been entered")
def enter_year(setup, monkeypatch):
    choice = StringIO('1952\n')
    monkeypatch.setattr('sys.stdin', choice)
    setup.get_birth_year()


@when('the number "2" is entered')
def enter_month(setup, monkeypatch):
    month = StringIO('2\n')
    monkeypatch.setattr('sys.stdin', month)
    setup.get_birth_month()



@then("the user is given a full retirement age")
def check_age(setup):
    assert setup.calculate_receipt_age(setup.year) == (66, 0)











@scenario('../features/data_entry.feature', 'Program rejects invalid year input')
def test_invalid_year():
    pass

@given(
    "the Full Retirement Age Calculator is started")
def running():
    pass


@when('the letter "a" is entered for year')
def year_setup(setup, monkeypatch):
    choice = StringIO('a\n')
    monkeypatch.setattr('sys.stdin', choice)
    setup.get_birth_year()



@then("the input is rejected")
def reject(setup):
    assert setup.year != 'a'







@scenario('../features/data_entry.feature', "Program rejects invalid month input")
def test_invalid_month():
    pass

@given("a valid year is entered")
def enter_year(setup, monkeypatch):
    choice = StringIO('1962\n')
    monkeypatch.setattr('sys.stdin', choice)
    setup.get_birth_year()


@when("the letter 'a' is entered")
def enter_month(setup, monkeypatch):
    month = StringIO('a\n')
    monkeypatch.setattr('sys.stdin', month)
    setup.get_birth_month()


@then("the input is rejected")
def verify_month(setup):
    assert setup.month != 'a'







@scenario('../features/data_entry.feature', "Program rejects too "
                                            "low year")
def test_low_year():
    pass


@given("the program is prompting for a year")
def step_impl():
    pass


@when("'1899' is entered")
def enter_year(setup, monkeypatch):
    choice = StringIO('1899\n')
    monkeypatch.setattr('sys.stdin', choice)
    setup.get_birth_year()


@then("the year entry is rejected")
def step_impl(setup):
    assert setup.year != 1899






@scenario('../features/data_entry.feature', "Program rejects too high year")
def test_high_year():
    pass


@given("the program is prompting for a year")
def step_impl():
    pass

@when("'2021' is entered")
def enter_year(setup, monkeypatch):
    choice = StringIO('2021')
    monkeypatch.setattr('sys.stdin', choice)
    setup.get_birth_year()

@then("the year entry is rejected")
def step_impl(setup):
    assert setup.year != 2021




@scenario('../features/data_entry.feature', "Program rejects too low month")
def test_low_month():
    pass

@given("the program is prompting for a month")
def step_impl():
    pass


@when("'0' is entered")
def enter_month(setup, monkeypatch):
    month = StringIO('0\n')
    monkeypatch.setattr('sys.stdin', month)
    setup.get_birth_month()


@then("the month entry is rejected")
def step_impl(setup):
    assert setup.month != 0



@scenario('../features/data_entry.feature', "Program rejects too "
                                            "high month")
def test_high_month():
    pass

@given("the program is prompting for a month")
def step_impl():
    pass


@when("'13' is entered")
def enter_month(setup, monkeypatch):
    month = StringIO('13\n')
    monkeypatch.setattr('sys.stdin', month)
    setup.get_birth_month()


@then("the month entry is rejected")
def step_impl(setup):
    assert setup.month != 13




@scenario('../features/data_entry.feature', 'Program accepts valid '
                                            'date entry on border')
def test_add():
    pass


@given("the Full Retirement Age Calculator is started")
def start():
    pass


@when('the year "1900" is entered')
def year_setup(setup, monkeypatch):
    choice = StringIO('1900\n')
    monkeypatch.setattr('sys.stdin', choice)
    setup.get_birth_year()



@then("the value is accepted")
def check_value(setup):
    assert setup.year  == 1900






@scenario('../features/data_entry.feature', 'Program accepts valid '
                                            'date entry for current year')
def test_add():
    pass


@given("the Full Retirement Age Calculator is started")
def start():
    pass


@when('the year "2020" is entered')
def year_setup(setup, monkeypatch):
    choice = StringIO('2020\n')
    monkeypatch.setattr('sys.stdin', choice)
    setup.get_birth_year()



@then("the value is accepted")
def check_value(setup):
    assert setup.year  == 2020
