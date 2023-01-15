Feature: Emag login feature

    Background:
      Given home: I am a user on emag.ro Home page

    @login1
    Scenario: Click logo button and return to home
      When home: I click on contul meu
      When login: I set my email "abc@email.com"
      When login: I click emag logo
      Then home: I verify home page url

    @login2
    Scenario: If a logged out user wants to buy a product, he has to login first
      When home: I hover over "Bacanie"
      When home: I click subcategory "Dulciuri"
      When products: I add product to basket "Biscuiti"
      When products: I click Vezi detalii cos
      When cart: I click checkout button
      Then login: I verify login page url



