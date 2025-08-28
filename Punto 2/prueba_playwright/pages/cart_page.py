from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page

    def open_cart(self):
        self.page.get_by_role("button", name=" 2 item(s) - $").click()

    def remove_macbook(self):
        self.page.get_by_role("row", name="MacBook Pro MacBook Pro x 1 $").get_by_role("button").click()
        self.page.screenshot(path="C:/Users/oscar/Documents/pantallazo_ejecucion/delete_MacBook_carrito..jpg")

    def view_cart(self):
        self.page.get_by_role("link", name=" View Cart").click()
