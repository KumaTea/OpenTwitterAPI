import json
from time import sleep
from app.static.common import *
from app.types.user import User
from seleniumwire.utils import decode
from app.session.manager import browser_manager


def list_friends(url: str, browser=None):
    """
    aka followed users
    """
    assert url.endswith('following')

    if not browser:
        browser = browser_manager.get_browser()
    browser.get(url)

    # Scroll to bottom until end
    t = -1  # pulled times
    while t <= len([i for i in browser.requests if 'Following' in i.path]):
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        t += 1
        sleep(SCROLL_DELAY)

    # Analyze HTTP requests
    requests = browser.requests
    following_requests = [i for i in requests if 'Following' in i.path]

    raw_users = []
    for request in following_requests:
        response = request.response
        decoded_response = decode(response.body, response.headers.get('Content-Encoding', 'identity'))
        users_data = json.loads(decoded_response)
        raw_users.extend(users_data['data']['user']['result']['timeline']['timeline']['instructions'][-1]['entries'])

    trimmed_raw_users = []
    for raw_user in raw_users:
        if raw_user['content']['entryType'] == 'TimelineTimelineItem':
            if raw_user['content']['itemContent']['itemType'] == 'TimelineUser':
                trimmed_raw_users.append(raw_user)

    users = []
    for raw_user in trimmed_raw_users:
        users.append(User(raw_user['content']['itemContent']['user_results']['result']))

    return users
