Feature: Emag Search Feature

    Background:
      Given home: I am a user on emag.ro Home page

    @search
    Scenario Outline: Test search functionality
      When home: I search after "<Query>"
      Then products: I check if the search contains the searched result "<Query>"

    Examples:
      |     Query     |
      | modulator     |
      | samsung       |

    @search_with_filter
    Scenario: Test search functionality with filter Brand and Price
      When home: I search after "laptop"
      When products: Filter by brand "Apple"
      And products: Activate the price range button
      And products: We select the slider on the right and enter the price "knob right" "-200"
      Then products: I check if the search contains the searched result "apple"
