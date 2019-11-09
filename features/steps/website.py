from behave import given, when, then

@when(u'I am on the url \'{url}\'')
def step_impl(context, url):
  """
    Navigate to the specified page
  """
  context.browser.get('http://localhost:5000' + url)

@then(u'load page of \'{url}\' is successful')
def step_impl(context, url):
  """
    The loaded page corresponds to the given URL.
  """
  print(context.browser.current_url)
  assert context.browser.current_url == 'http://localhost:5000' + url

@then(u'I read "{text}"')
def step_impl(context, text):
  assert text in context.browser.page_source