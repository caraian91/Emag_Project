Feature: Emag favorites cart feature

  Background:
    Given home: I am a user on emag.ro Home page

  @favorites
  Scenario: Click on a favorite product, then from favorite cart we will add to cart the product and delete from favorites
    When home: I hover over "Laptop, Tablete & Telefoane"
    When home: I click subcategory "Laptopuri"
    When products: I add to favorites cart the laptop "ASUS X515MA-EJ450"
    When products: I click Produse Favorite
    When login: I check that i have reached the favorites page url
    When products: I click on the button Add to Basket from Favorites "ASUS X515MA-EJ450"
    Then products: I click on the delete buton from Favorites "ASUS X515MA-EJ450"