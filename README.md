# CS50W Project-2: Commerce

This is Project 2 in the HarvardX course CS50W - CS50's Web Programming with Python and JavaScript

[Video Demo](https://youtu.be/FwHufzlC34M)

### CS50W's Project 2 specifications
[CS50W Project 2](https://cs50.harvard.edu/web/2020/projects/2/commerce/)

#### Description:
This application is an eBay-like e-commerce auction site that will allow users to post auction listings, place bids on listings, comment on those listings, and add listings to a “watchlist.”

* Models: Your application should have at least three models in addition to the User model: one for auction listings, one for bids, and one for comments made on auction listings. It’s up to you to decide what fields each model should have, and what the types of those fields should be. You may have additional models if you would like.

* Create Listing: Users should be able to visit a page to create a new listing. They should be able to specify a title for the listing, a text-based description, and what the starting bid should be. Users should also optionally be able to provide a URL for an image for the listing and/or a category (e.g. Fashion, Toys, Electronics, Home, etc.).
  
![Create](https://github.com/sam-aum/Commerce-Project-2/assets/95770704/21da9904-ade3-40bd-87ea-ca1a1b9d7231)

* Active Listings Page: The default route of your web application should let users view all of the currently active auction listings. For each active listing, this page should display (at minimum) the title, description, current price, and photo (if one exists for the listing).
  
![Active Listings](https://github.com/sam-aum/Commerce-Project-2/assets/95770704/1705ae1c-335f-4e75-8ff1-a08ac325e42d)

* Listing Page: Clicking on a listing should take users to a page specific to that listing. On that page, users should be able to view all details about the listing, including the current price for the listing.
  * If the user is signed in, the user should be able to add the item to their “Watchlist.” If the item is already on the watchlist, the user should be able to remove it.
  * If the user is signed in, the user should be able to bid on the item. The bid must be at least as large as the starting bid, and must be greater than any other bids that have been placed (if any). If the bid doesn’t meet those criteria, the user should be presented with an error.
  * If the user is signed in and is the one who created the listing, the user should have the ability to “close” the auction from this page, which makes the highest bidder the winner of the auction and makes the listing no longer active.
  * If a user is signed in on a closed listing page, and the user has won that auction, the page should say so.
  * Users who are signed in should be able to add comments to the listing page. The listing page should display all comments that have been made on the listing.

![Listing](https://github.com/sam-aum/Commerce-Project-2/assets/95770704/2946664f-3fe5-4741-a14f-763695b7919f)

* Watchlist: Users who are signed in should be able to visit a Watchlist page, which should display all of the listings that a user has added to their watchlist. Clicking on any of those listings should take the user to that listing’s page.
  
![Watchlist](https://github.com/sam-aum/Commerce-Project-2/assets/95770704/df104266-8e5c-414e-a111-40f1689367e4)

* Categories: Users should be able to visit a page that displays a list of all listing categories. Clicking on the name of any category should take the user to a page that displays all of the active listings in that category.

* Django Admin Interface: Via the Django admin interface, a site administrator should be able to view, add, edit, and delete any listings, comments, and bids made on the site.
  
![Admin](https://github.com/sam-aum/Commerce-Project-2/assets/95770704/c4de3d5c-dfc7-4dc1-b908-bc1a21985f56)

