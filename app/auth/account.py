from typing import Union
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
