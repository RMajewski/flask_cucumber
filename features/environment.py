import os
import threading

from wsgiref import simple_server
from wsgiref.simple_server import WSGIRequestHandler

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from app import app

# Optionen für Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-proxy-server")
chrome_options.add_argument("--prox-server='direct://'")
chrome_options.add_argument("--prox-bypass-list=*")

def before_all(context):
  context.server = simple_server.WSGIServer(("", 5000), WSGIRequestHandler)
  context.server.set_app(app)
  context.pa_app = threading.Thread(target=context.server.serve_forever)
  context.pa_app.start()

  context.browser = webdriver.Chrome(options=chrome_options, executable_path=ChromeDriverManager().install())
  context.browser.set_page_load_timeout(time_to_wait=2)

def after_all(context):
  context.browser.quit()
  context.server.shutdown()
  context.pa_app.join()