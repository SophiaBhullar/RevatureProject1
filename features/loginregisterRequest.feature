Feature: As an employee, I should be able to submit requests

    Scenario: From the submit request page I create a new request with valid inputs
        Given I am on submit request page
        When I input in a valid employee ID
        When I input in a valid description
        When I input in a valid amount
        When I input in a valid status
        When I input in a valid comments
        When I click on sumit button
        Then I should have a success response