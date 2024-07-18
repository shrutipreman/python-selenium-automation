
Feature: Target main page different feature test

  Scenario: Cart empty then 'Your cart is empty' message displayed
    Given Open target main page
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown

  Scenario:  logged out user can navigate to Sign In
    Given Open target main page
    When Click Sign In
    And right side navigation menu, click Sign In
    Then Verify Sign In form opened