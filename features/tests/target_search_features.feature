Feature: Target main page search tests

  Scenario: User can search for chocolate
    Given Open target main page
    When Search for chocolate
    Then Verify search results shown for chocolate
    Then Verify correct search results URL opens for chocolate


  Scenario: User can search for a chips
    Given Open target main page
    When Search for chips
    Then Verify search results shown for chips
    Then Verify correct search results URL opens for chips

  Scenario: User can search for an pen
    Given Open target main page
    When Search for pen
    Then Verify search results shown for pen
    And Verify correct search results URL opens for pen

