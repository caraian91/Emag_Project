Feature: Emag Cart Feature

    Background:
      Given home: I am a user on emag.ro Home page
      When home: I search after "iPhone 14, 128GB, Gold"
      When products: I add product to basket "Telefon mobil Apple iPhone 14 Pro, 128GB, 5G, Gold"
      When products: I click Vezi detalii cos

    @cart_price
    Scenario: Test cart total price functionality
      Then cart: I verify that total price is correct "6.299,99"


    @cart_remove
    Scenario: Test cart remove product functionality
      When cart: I click sterge link
      Then cart: I verify empty cart message is displayed




