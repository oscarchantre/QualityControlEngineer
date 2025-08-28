from playwright.sync_api import Page
import time

class ResetPass:
    def __init__(self, page: Page):
        self.page = page

    def reset_password(self, new_password):
        #self.page.goto("http://opencart.abstracta.us/index.php?route=account/success")
        self.page.get_by_role("link", name="Continue").click()
        time.sleep(6)
        self.page.locator("#content").get_by_role("link", name="Password").click()
        self.page.get_by_role("textbox", name="* Password", exact=True).fill(new_password)
        self.page.get_by_role("textbox", name="* Password Confirm").fill(new_password)
        self.page.get_by_role("button", name="Continue").click()
        time.sleep(2)
        self.page.screenshot(path="C:/Users/oscar/Documents/pantallazo_ejecucion/Restablecer_password.jpg")
