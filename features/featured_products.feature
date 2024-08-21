

Feature: Featured Products

  Background:
    Given I am on the home page

  @FEATURED_PRODUCTS_FEATURE
  Scenario Outline: Check that when you click on any Featured Products item, you are actually accessing that product's webpage
    When I click on "<Featured_Product>" button
    Then I should access "<Featured_Product_Item>" webpage
    Examples:
      |Featured_Product | Featured_Product_Item |
      |Build your own computer | Build your own computer |
      |Apple MacBook Pro 13-inch | Apple MacBook Pro 13-inch |
      |HTC One M8 Android L 5.0 Lollipop | HTC One M8 Android L 5.0 Lollipop |
      |$25 Virtual Gift Card | $25 Virtual Gift Card |





