from app.sess.browser import new_browser, new_incognito


class BrowserManager:
    def __init__(self):
        self.browser = None
        self.incognito = None

    def get_browser(self, existing=False):
        if not existing:
            self.quit()
            self.browser = new_browser()
        return self.browser

    def get_incognito(self, existing=False):
        if not existing:
            self.quit()
            self.incognito = new_incognito()
        return self.incognito

    def quit(self):
        if self.browser:
            self.browser.quit()
        self.browser = None

    def quit_incognito(self):
        if self.incognito:
            self.incognito.quit()
        self.incognito = None


browser_manager = BrowserManager()
