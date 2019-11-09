from behave import given, when, then

@when(u'I am on the url \'{url}\'')
def step_impl(context, url):
  """
    Navigate to the specified page
  """
  context.browser.get('http://localhost:5000' + url)


@then(u'I should get a \'{code}\' response')
def step_impl(context, code):
  """
    Check if the expected HTTP status code was returned.
  """
  print(dir(context.browser))
  assert False
  