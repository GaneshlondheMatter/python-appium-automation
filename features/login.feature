Feature: Login functionality

  Scenario: Successful login with valid credentials
    Given user launches the application
    When user enters valid username and password
    And clicks on login button
    Then user should be navigated to dashboard