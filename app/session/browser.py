from selenium import webdriver
from app.conf.config import get_config, get_chrome_options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


general_config = get_config('GENERAL')
data_dir = general_config['data_dir']
profile_name = general_config['profile_name']


def get_browser():
    service = ChromeService(ChromeDriverManager().install())
    options = get_chrome_options(data_dir, profile_name)
    return webdriver.Chrome(service=service, options=options)
