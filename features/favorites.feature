Feature: Emag favorites cart feature

  Background:
    Given home: I am a user on emag.ro Home page

  @favorites
  Scenario: Click on a favorite product, then from favorite cart we will add to cart the product and delete from favorites
    When home: I hover over "Laptop, Tablete & Telefoane"
    When home: I click subcategory "Laptopuri"
    When favorite: I add to favorites cart the laptop "Lenovo V15 G2 ITL"
    When favorite: I click on Produse Favorite
    When favorite: I check that i have reached the favorites page url
    When favorite: I click on the button Add to Basket from Favorites "Lenovo V15 G2 ITL"
    And favorite: I check the message on the basket to see that it has been added "1"
    Then favorite: I click on the delete buton from Favorites "Lenovo V15 G2 ITL"