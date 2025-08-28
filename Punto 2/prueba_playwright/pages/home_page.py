from playwright.sync_api import Page
import time

class HomePage:
    def __init__(self, page: Page):
        self.page = page


    def open(self):
        self.page.goto("https://opencart.abstracta.us/")
 

    def go_to_register(self):
        self.page.get_by_role("link", name=" My Account").click()
        self.page.get_by_role("link", name="Register").click()

    def search_product(self, product: str):
        self.page.get_by_role("textbox", name="Search").fill(product)
        self.page.get_by_role("button", name="").click()
