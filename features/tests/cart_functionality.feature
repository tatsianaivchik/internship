# Created by TANYA at 4/25/23
Feature: Shopping cart tests

  Scenario: Adding eye gel product in the cart and verify product and price
    Given Open CURESKIN main page
    When Close pop up window
    And Click on search icon
    And Input text eye gel
    And Click on first product
    And Store product name and price
    And Add product to the cart
    And Open Cart page
    Then Verify that 1 items shown
    Then Verify product name and price

  Scenario: Adding Cream product in the cart and verify product and price
    Given Open CURESKIN main page
    When Close pop up window
    And Click on search icon
    And Input text cream
    And Click on first product
    And Store product name and price
    And Add product to the cart
    And Open Cart page
    Then Verify that 1 items shown
    Then Verify product name and price

