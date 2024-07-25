Feature: Product added to cart
  Scenario: User checks if product in cart
    Given Open target main page
    When Search for chocolate
    And Add product to cart
    And Add to cart from side navigation
    And Open cart page
    Then Verify  1 item is present in cart