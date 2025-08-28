from playwright.sync_api import Page
import time

class RegisterPage:
    def __init__(self, page: Page):
        self.page = page

    def fill_registration_form(self, firstname, lastname, email, phone, password):
        self.page.get_by_role("textbox", name="* First Name").fill(firstname)
        self.page.get_by_role("textbox", name="* Last Name").fill(lastname)
        self.page.get_by_role("textbox", name="* E-Mail").fill(email)
        self.page.get_by_role("textbox", name="* Telephone").fill(phone)
        self.page.get_by_role("textbox", name="* Password", exact=True).fill(password)
        self.page.get_by_role("textbox", name="* Password Confirm").fill(password)
        self.page.get_by_role("checkbox").check()
        self.page.get_by_role("button", name="Continue").click()
        self.page.screenshot(path="C:/Users/oscar/Documents/pantallazo_ejecucion/Registro.jpg")
        time.sleep(6)
