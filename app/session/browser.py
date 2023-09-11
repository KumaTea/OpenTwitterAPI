from seleniumwire import webdriver
from app.conf.config import get_config, get_chrome_options
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox imports GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service imports Service as FirefoxService


general_config = get_config('GENERAL')
data_dir = general_config['data_dir']
profile_name = general_config['profile_name']


def new_browser():
    service = ChromeService(ChromeDriverManager().install())
    # service = FirefoxService(GeckoDriverManager().install())
    options = get_chrome_options(data_dir, profile_name)
    # options = get_firefox_options(data_dir, profile_name)
    return webdriver.Chrome(service=service, options=options)


def new_incognito():
    service = ChromeService(ChromeDriverManager().install())
    # service = FirefoxService(GeckoDriverManager().install())
    options = get_chrome_options(data_dir, profile_name)
    # options = get_firefox_options(data_dir, profile_name)
    options.add_argument('--incognito')
    return webdriver.Chrome(service=service, options=options)
