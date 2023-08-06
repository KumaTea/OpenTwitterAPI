from typing import Union
import app.static.urls as URLS
from app.sess.manager import browser_manager
from app.conf.config import get_config, set_config
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def set_account(username: str, password: str):
    section = 'ACCOUNT'
    items = {'username': username, 'password': password}
    set_config(section, items)
    return True


def try_login(
    username: Union[str, None] = None,
    password: Union[str, None] = None,
):
    if not (username and password):
        try:
            username = get_config('ACCOUNT')['username']
            password = get_config('ACCOUNT')['password']
        except KeyError:
            raise KeyError('Username and password not set')

    browser = browser_manager.get_browser()
    browser.get(URLS.login)

    username_input = browser.find_element(By.NAME, 'text')
    username_input.send_keys(username)

    next_button = browser.find_element(By.XPATH, '//div[@role="button"]')
    next_button.send_keys(Keys.ENTER)
