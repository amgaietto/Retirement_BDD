Feature: Retirement Date Return
As a user, I want to receive the month and year of my projected retirement age.

	Background:
	Given the Full Retirement Age Calculator has started



	Scenario Outline: Ensure correct month of retirement is given
		When the year, month "<year>", "<month>" of birth is entered
		Then the date of retirement displayed is "<final_month>","<final_year>"



	Examples: Months
		| year | month |final_month   | final_year |
		| 1937 | 12    |December      | 2002       |
		| 1937 | 1     |January       | 2002       |
		| 1955 | 5     |July          | 2021       |
		| 1960 | 11    |November      | 2027       |
