# initialize the conf.ini file

import random
import string
import configparser
from typing import Union
from app.conf.default import *
from seleniumwire import webdriver
from app.conf.config import get_chrome_options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


def gen_uuid(length=4):
    # https://stackoverflow.com/a/56398787/10714490
    alphabet = string.ascii_lowercase + string.digits
    return ''.join(random.choices(alphabet, k=length))


def init_config(
        # project_dir: Union[str, None] = None,
        # config_file: Union[str, None] = None,
        data_dir: Union[str, None] = None,
        profile_name: Union[str, None] = None):
    # project_dir = project_dir or PROJECT_DIR
    project_dir = PROJECT_DIR
    config_file = CONFIG_FILE
    data_dir = data_dir or DATA_DIR
    profile_name = profile_name or gen_uuid()

    # create config dir
    # os.makedirs(os.path.join(get_home_dir(), project_dir), exist_ok=True)
    # create data dir
    os.makedirs(os.path.join(get_home_dir(), project_dir, data_dir), exist_ok=True)

    # write config file
    config = configparser.ConfigParser()
    config['GENERAL'] = {
        'profile_name': profile_name,
        'data_dir': data_dir,
        'project_dir': project_dir,
        'config_file': config_file,
    }
    with open(CONFIG_FILE_PATH, 'w') as f:
        config.write(f)

    return data_dir, profile_name


def init_browser(data_dir, profile_name):
    service = ChromeService(ChromeDriverManager().install())
    options = get_chrome_options(data_dir, profile_name)

    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://twitter.com/')
    driver.quit()
    return driver


def initialize(
        data_dir: Union[str, None] = None,
        profile_name: Union[str, None] = None):
    data_dir, profile_name = init_config(data_dir=data_dir, profile_name=profile_name)
    driver = init_browser(data_dir=data_dir, profile_name=profile_name)
    return driver
