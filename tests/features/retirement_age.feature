Feature: Full Retirement Age Return
As a user, I want to receive my full retirement age.

	Background:
	Given the Full Retirement Age Calculator has started
	

	Scenario Outline: Correct age of retirement is returned
		When the year "<year>" is entered
		Then the full retirement age displayed is "<years>", "<month>"

	Examples: Dataset
		| year | years   | month |
		| 1937 | 65      |  0	 |
		| 1943 | 66      |  0    |
		| 1955 | 66      |  2    |
		| 1960 | 67      |  0    |
