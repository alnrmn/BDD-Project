Feature: Register feature

  Background:
    Given I am on the register page

  @SMOKE_TEST @REGISTER_FEATURE
  Scenario: Register a new account by filling in all mandatory fields
    When I fill in "Cornel" in First Name field
    And I fill in "Johnson" in Last Name field
    And I fill in "cornel@johns.com" in Email field
    And I fill in "123456" in Password field
    And I fill in "123456" in Confirm password field
    And I click on the Register button
    Then I should see a registration confirmation message


  @NEGATIVE_TEST @REGISTER_FEATURE
  Scenario: Register without filling in a Last name
    When I fill in "Gelu" in First Name field
    And I leave blank the Last Name field
    And I fill in "gelu@jddsssc.com" in Email field
    And I fill in "123456" in Password field
    And I fill in "123456" in Confirm password field
    And I click on the Register button
    Then I should see an error message