Feature: Register feature

  Background:
    Given I am on the register page

  @SMOKE_TEST @REGISTER_FEATURE
  Scenario: Register a new account by filling in all mandatory fields
    When I fill in "Harry" in First Name field
    And I fill in "Johnson" in Last Name field
    And I fill in "harry@johns.com" in Email field
    And I fill in "123456" in Password field
    And I fill in "123456" in Confirm password field
    And I click on the Register button
    Then I should see a registration confirmation message


  @NEGATIVE_TEST @REGISTER_FEATURE
  Scenario: Register without filling in a Last name
    When I fill in "Marcel" in First Name field
    And I leave blank the Last Name field
    And I fill in "marcel@jddssc.com" in Email field
    And I fill in "123456" in Password field
    And I fill in "123456" in Confirm password field
    And I click on the Register button
    Then I should see an error message
