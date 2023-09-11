from time import sleep
from typing import Union
import app.static.urls as URLS
from app.static.common import *
from app.imports.webdriver import *
from app.session.manager import browser_manager
from app.conf.config import get_config, set_config


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

    # username_input = browser.find_element(By.NAME, 'text')
    username_input = WebDriverWait(browser, DELAY).until(EC.visibility_of_element_located((By.NAME, 'text')))
    username_input.send_keys(username)

    # next_button = browser.find_element(By.XPATH, '//div[@role="button"]')
    # next_button.send_keys(Keys.ENTER)
    username_input.send_keys(Keys.ENTER)

    # password_input = browser.find_element(By.NAME, 'password')
    password_input = WebDriverWait(browser, DELAY).until(EC.visibility_of_element_located((By.NAME, 'password')))
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)

    # DO NOT QUIT BROWSER!!!

    sleep(DELAY)
    password_input = None
    verify_input = None
    try:
        password_input = browser.find_element(By.NAME, 'password')
    except e.NoSuchElementException:
        pass
    try:
        verify_input = browser.find_element(By.XPATH, '//input[@inputmode="numeric"]')
    except e.NoSuchElementException:
        pass

    if password_input:
        # password error
        browser_manager.quit()
        return 403, 'Password input still exists, maybe password is wrong?'
    elif verify_input:
        # 2fa code required
        return 401, 'Two step verification code required, call try_2fa(code).'


def try_2fa(code: str):
    browser = browser_manager.get_browser(existing=True)
    verify_input = browser.find_element(By.XPATH, '//input[@inputmode="numeric"]')
    verify_input.send_keys(code)
    verify_input.send_keys(Keys.ENTER)

    # DO NOT QUIT BROWSER!!!

    sleep(DELAY)
    verify_input = None
    try:
        verify_input = browser.find_element(By.XPATH, '//input[@inputmode="numeric"]')
    except e.NoSuchElementException:
        pass

    if verify_input:
        # 2fa code error
        browser_manager.quit()
        return 403, 'Verification code input still exists, maybe code is wrong?'

    login_success = False
    current_url = browser.current_url
    if current_url == URLS.home:
        login_success = True

    if login_success:
        set_config('ACCOUNT', {'logged_in': 'True'})
        return 200, 'Login success'
    else:
        return 500, 'Login failed, unknown error'
