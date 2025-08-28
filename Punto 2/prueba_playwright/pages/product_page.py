from playwright.sync_api import Page

class ProductPage:
    def __init__(self, page: Page):
        self.page = page

    def add_macbook_pro_to_cart(self):
        self.page.get_by_role("link", name="Laptops & Notebooks", exact=True).click()
        self.page.get_by_role("link", name="Show All Laptops & Notebooks").click()
        self.page.get_by_role("button", name=" Add to Cart").nth(3).click()
        self.page.screenshot(path="C:/Users/oscar/Documents/pantallazo_ejecucion/sección_Laptops_Notebooks.jpg")

    def add_search_result_to_cart(self):
        self.page.get_by_role("button", name=" Add to Cart").click()
        self.page.screenshot(path="C:/Users/oscar/Documents/pantallazo_ejecucion/Agg_carrito_portátil_MacBook.jpg")
