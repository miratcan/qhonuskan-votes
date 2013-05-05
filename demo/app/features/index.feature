Feature: Rocking with qhonuskan_votes

  Scenario: Voting as AnonymousUser
    Given I access the url "/"
    When I tried to vote "1"
    Then response status code is "401"

  Scenario: Voting as super user
    Given following users exist:
      | username | is_superuser | is_active |
      | admin    | True         | True      |
    And I logined as "admin"
    And I access the url "/"
    When I tried to vote "1"
    Then response status code is "200"

  Scenario: Voting a model two times with same user
    Given following users exist:
      | username | is_superuser | is_active |
      | admin    | True         | True      |
      | gokmen   | False        | True      |
      | mirat    | False        | False     |
    And I logined as "admin"
    When I tried to vote "1"
    Then response status code is "200"
    When I tried to vote "1"
    Then response status code is "200"
