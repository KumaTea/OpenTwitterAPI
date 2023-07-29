from app.sess.browser import get_browser, get_incognito_browser


class BrowserManager:
    def __init__(self):
        self.browser = None
        self.incognito_browser = None

    def get_browser(self):
        if not self.browser:
            self.browser = get_browser()
        return self.browser

    def get_incognito_browser(self):
        if not self.incognito_browser:
            self.incognito_browser = get_incognito_browser()
        return self.incognito_browser

    def quit(self):
        if self.browser:
            self.browser.quit()
        if self.incognito_browser:
            self.incognito_browser.quit()
        self.browser = None
        self.incognito_browser = None
