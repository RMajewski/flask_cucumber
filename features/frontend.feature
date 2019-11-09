Feature: View the website
  View the login page
  As an anonymous user
  I would like to see the login page when entering the URL.

Scenario: Response 200 then call the website
  When I am on the url '/'
  Then I should get a '200' response
