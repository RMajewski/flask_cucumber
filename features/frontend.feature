Feature: View the website
  View the login page
  As an anonymous user
  I would like to see the login page when entering the URL.

Scenario: Load page is successful
  When I am on the url '/'
  Then load page of '/' is successful
  And I read "Hallo Welt"
