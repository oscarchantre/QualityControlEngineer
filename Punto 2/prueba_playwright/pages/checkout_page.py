from playwright.sync_api import Page
import time

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    def fill_checkout_form(self, firstname, lastname, company, address, city, postcode, country, region):
        self.page.get_by_role("textbox", name="* First Name").fill(firstname)
        self.page.get_by_role("textbox", name="* Last Name").fill(lastname)
        self.page.get_by_role("textbox", name="Company").fill(company)
        self.page.get_by_role("textbox", name="* Address").fill(address)
        self.page.get_by_role("textbox", name="* City").fill(city)
        self.page.get_by_role("textbox", name="* Post Code").fill(postcode)
        self.page.get_by_label("Country").select_option(country)
        self.page.get_by_label("Region / State").select_option(region)
        self.page.get_by_role("button", name="Continue").click()
        self.page.get_by_role("button", name="Continue").click()
        self.page.get_by_role("button", name="Continue").click()
        self.page.get_by_role("checkbox").check()
        self.page.get_by_role("button", name="Continue").click()
        self.page.get_by_role("button", name="Confirm Order").click()
        time.sleep(6)
        self.page.screenshot(path="C:/Users/oscar/Documents/pantallazo_ejecucion/Proceso_compra.jpg")
        self.page.get_by_role("link", name="Continue").click()
        self.page.screenshot(path="C:/Users/oscar/Documents/pantallazo_ejecucion/final.jpg")
