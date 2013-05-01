Feature: Rocking with qhonuskan_votes

    Scenario: Voting as AnonymousUser
        Given I access the url "/"
        Then I cannot vote "1"
