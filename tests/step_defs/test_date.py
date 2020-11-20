from pytest_bdd import scenario, given, when, then, parsers


EXTRA_TYPES = {
    'Number' : int,
    'Str': str
}

CONVERTERS = {
    'year': int,
    'final_month': str,
    'final_year': int
}



@scenario('../features/retirement_date.feature', 'Ensure correct month of retirement is given')
def test_dates():
    pass

@given('the Full Retirement Age Calculator has started')
def step_impl():
    pass


@when(parsers.cfparse('the year, month "{year:Number}", '
                      '"{month:Number}" of '
                      'birth is entered', extra_types=EXTRA_TYPES))
@when('the year, month "<year>", "<month>" of birth is entered')
def enter_data(setup, year, month):
    year = int(year)
    month = int(month)
    setup.calculate_retirement_date(year, month)

@then('the date of retirement displayed is "<final_month>","<final_year>"')
@then(parsers.cfparse('the date of retirement displayed is "{'
            'final_month:Str}", '
      '"{final_year:Number}"', extra_types=EXTRA_TYPES))
def get_final(setup, final_month, final_year):
    final_year = int(final_year)
    assert setup.final_year == final_year
    assert setup.final_month == final_month

