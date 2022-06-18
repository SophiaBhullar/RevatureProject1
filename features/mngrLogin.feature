Feature: User wants to login as manager

    
    Scenario:User wants to login in as manager
        Given user is on manager login page
        When user enter designation as "Manager"
        When user enter Username as "Ajay"
        When user enter Password as "Ajay1234"
        When user click on manager LOGIN button
        Then User can see view request page
        