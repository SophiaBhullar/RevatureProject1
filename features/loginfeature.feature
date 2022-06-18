Feature: User wants to login as employee

    
    Scenario:User wants to login in 
        Given user is on login page
        When user enter designation as "Employee"
        When user enter Username as "Sophia"
        When user enter Password as "Sophia1234"
        When user click on LOGIN button
        Then User can see fill request page
        