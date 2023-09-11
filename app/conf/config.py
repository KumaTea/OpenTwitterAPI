import configparser
from app.conf.default import *
from seleniumwire import webdriver
from app.static.browser import UA, HEIGHT, WIDTH


def get_config(section: str):
    section = section.upper()
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE_PATH)
    return dict(config[section])


def set_config(section: str, items: dict):
    section = section.upper()
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE_PATH)
    if section in config and config[section]:
        config[section].update(items)
    else:
        config[section] = items
    with open(CONFIG_FILE_PATH, 'w') as f:
        config.write(f)


def get_chrome_options(data_dir, profile_name):
    options = webdriver.ChromeOptions()
    options.add_argument(f'--user-data-dir={os.path.join(get_home_dir(), PROJECT_DIR, data_dir, profile_name)}')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--headless=new')
    mobile_emulation = {'deviceName': 'Pixel 5'}
    options.add_experimental_option('mobileEmulation', mobile_emulation)
    return options


def get_firefox_options(data_dir, profile_name):
    options = webdriver.FirefoxOptions()
    # options.add_argument(f'--profile={os.path.join(get_home_dir(), PROJECT_DIR, data_dir, profile_name)}')
    # options.set_preference('profile', os.path.join(get_home_dir(), PROJECT_DIR, data_dir, profile_name))
    options.add_argument("--width=" + str(WIDTH))
    options.add_argument("--height=" + str(HEIGHT))
    # options.headless = True

    profile = webdriver.FirefoxProfile(
        profile_directory=os.path.join(get_home_dir(), PROJECT_DIR, data_dir, profile_name))
    profile.set_preference('general.useragent.override', UA)
    options.profile = profile

    return options
