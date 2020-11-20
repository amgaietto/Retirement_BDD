from pytest_bdd import scenario, given, when, then, scenarios, parsers
from retirement_class import Retiree
import pytest


EXTRA_TYPES = {
    'Number' : int,
}

CONVERTERS = {
    'year': int,
    'years': int,
    'month': int
}

@scenario('../features/retirement_age.feature', 'Correct age of '
                                                'retirement is returned')
def test_ranges():
    pass


@given('the Full Retirement Age Calculator has '
                      'started')
def step_impl():
    pass



@when(parsers.cfparse('the year "{year:Number}" is entered',
                      extra_types=EXTRA_TYPES))
@when('the year "<year>" is entered')
def enter_year(setup, year):
    year = int(year)
    setup.calculate_receipt_age(year)

@then(parsers.cfparse('the full retirement age displayed is "{'
                      'years:Number}","{month:Number}"',
                      extra_types=EXTRA_TYPES))
@then('the full retirement age displayed is "<years>", "<month>"')
def step_impl(setup, years, month):
    years = int(years)
    month = int(month)
    assert setup.age == years
    assert setup.months == month
