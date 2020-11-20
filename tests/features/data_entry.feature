Feature: Data Entry
 As a user, I want to be able to enter my year and month of birth to determine when I can retire.

	Scenario: Program accepts valid date entry
		Given the Full Retirement Age Calculator is started
		When the year "1987" is entered
		Then the value is accepted

	Scenario: Program accepts valid month entry
		Given a valid year has been entered
		When the number "2" is entered
		Then the user is given a full retirement age


	#I was not able to test the following two items as they would
 # have required my interaction from the command line. If I were on
# a website so I could use selenium, etc., I would be testing that
# various text prompting the user to do actions would be on the
# screen.
	#Scenario: Program allows user to add additional years
		#Given a valid year and month of birth have been entered
		#When the year "1956" is entered
		#Then the user is prompted to enter a month of birth

	#Scenario: Program exits when prompted
		#Given the Full Retirement Calculator is prompting for year
		#When "return" is hit
		#Then the program exits

	Scenario: Program rejects invalid year input
		Given the Full Retirement Age Calculator is started
		When the letter "a" is entered for year
		Then the input is rejected

	Scenario: Program rejects invalid month input
		Given a valid year is entered
		When the letter 'a' is entered
		Then the input is rejected

	Scenario: Program rejects too low year
		Given the program is prompting for a year
		When '1899' is entered
		Then the year entry is rejected

	Scenario: Program rejects too high year
		Given the program is prompting for a year
		When '2021' is entered
		Then the year entry is rejected

	Scenario: Program rejects too low month
		Given the program is prompting for a month
		When '0' is entered
		Then the month entry is rejected

	Scenario: Program rejects too high month
		Given the program is prompting for a month
		When '13' is entered
		Then the month entry is rejected

	Scenario: Program accepts valid date entry on border
		Given the Full Retirement Age Calculator is started
		When the year "1900" is entered
		Then the value is accepted


	Scenario: Program accepts valid date entry for current year
		Given the Full Retirement Age Calculator is started
		When the year "2020" is entered
		Then the value is accepted
