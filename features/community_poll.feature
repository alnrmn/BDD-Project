Feature: Community poll feature

  Background:
    Given I am on the home page

  @INTEGRATION_TEST @NEGATIVE_TEST @COMMUNITY_POLL_FEATURE
  Scenario Outline: Try to vote in the Community poll as a visitor (not logged in)
    When I click on the "<Poll_Answer>" poll button
    And I click on the Vote button
    Then I should see a voting error message
    Examples:
    | Poll_Answer |
    | Excellent |
    | Good |
    | Poor |
    | Very bad |