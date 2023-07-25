import configparser
from app.conf.default import *
from selenium import webdriver


def get_config(section: str):
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE_PATH)
    return dict(config[section])


def get_chrome_options(data_dir, profile_name):
    options = webdriver.ChromeOptions()
    options.add_argument(f'--user-data-dir={os.path.join(get_home_dir(), PROJECT_DIR, data_dir, profile_name)}')
    # options.add_argument('--no-sandbox')
    options.add_argument('--headless=new')
    mobile_emulation = {'deviceName': 'Pixel 5'}
    options.add_experimental_option('mobileEmulation', mobile_emulation)
    return options
