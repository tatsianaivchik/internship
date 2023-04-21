# Created by TANYA at 4/20/23
Feature: CURESKIN search tests

  Scenario: User can search item on CURESKIN page
    Given Open CURESKIN main page
    When Close pop up window
    When Click on search icon
    When Input text SPF
    Then Verify SPF item(s) is shown

