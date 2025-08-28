import pytest
import re
import time
from playwright.sync_api import Page, expect


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {"ignore_https_errors": True}


def test_example(page: Page) -> None:
    page.goto("https://opencart.abstracta.us/")
    
    #Completa el formulario de registro.
    page.get_by_role("link", name=" My Account").click()
    page.get_by_role("link", name="Register").click()
    page.get_by_role("textbox", name="* First Name").click()
    page.get_by_role("textbox", name="* First Name").fill("Juan")
    page.get_by_role("textbox", name="* Last Name").click()
    page.get_by_role("textbox", name="* Last Name").fill("Perez")
    page.get_by_role("textbox", name="* E-Mail").click()
    page.get_by_role("textbox", name="* E-Mail").fill("Juanperez16@yopmail.com")
    page.get_by_role("textbox", name="* Telephone").click()
    page.get_by_role("textbox", name="* Telephone").fill("123457890")
    page.get_by_role("textbox", name="* Password", exact=True).click()
    page.get_by_role("textbox", name="* Password", exact=True).press("CapsLock")
    page.get_by_role("textbox", name="* Password", exact=True).fill("1234567890")
    page.get_by_role("textbox", name="* Password Confirm").click()
    page.get_by_role("textbox", name="* Password Confirm").fill("1234567890")
    page.get_by_role("checkbox").check()
    page.get_by_role("button", name="Continue").click()
    time.sleep(5)
    page.goto("http://opencart.abstracta.us/index.php?route=account/success")
    page.get_by_role("link", name="Continue").click()
    time.sleep(6)

    #Prueba el restablecimiento de contraseña.

    page.locator("#content").get_by_role("link", name="Password").click()
    page.goto("https://opencart.abstracta.us/index.php?route=account/password")
    page.get_by_role("textbox", name="* Password", exact=True).click()
    page.get_by_role("textbox", name="* Password", exact=True).fill("123456789")
    page.get_by_role("textbox", name="* Password Confirm").click()
    page.get_by_role("textbox", name="* Password Confirm").fill("123456789")
    page.get_by_role("button", name="Continue").click()

    #selecciona la opción “Show all laptops & notebooks”
    page.get_by_role("link", name="Laptops & Notebooks", exact=True).click()
    page.get_by_role("link", name="Show All Laptops & Notebooks").click()
    #Agrega al carrito de compras un portátil MacBook Pro.
    page.goto("http://opencart.abstracta.us/index.php?route=product/category&path=18")
    page.get_by_role("button", name=" Add to Cart").nth(3).click()

    #búscar y agregar al carrito de compras una tablet Samsung Galaxy.
    page.get_by_role("textbox", name="Search").click()
    page.get_by_role("textbox", name="Search").fill("Samsung Galaxy")
    page.get_by_role("button", name="").click()
    page.get_by_role("button", name=" Add to Cart").click()
    #Elimina la MacBook Pro del carrito.
    page.get_by_role("button", name=" 2 item(s) - $").click()
    page.get_by_role("row", name="MacBook Pro MacBook Pro x 1 $").get_by_role("button").click()
    #Agrega otra unidad de la tablet Samsung Galaxy.
    page.get_by_role("button", name=" Add to Cart").click()
    page.get_by_role("button", name=" 2 item(s) - $").click()
    page.get_by_role("link", name=" View Cart").click()
    #Completa el proceso de compra hasta la confirmación de la orden.
    page.get_by_role("link", name="Checkout", exact=True).click()
    page.goto("https://opencart.abstracta.us/index.php?route=checkout/checkout")
    page.get_by_role("textbox", name="* First Name").click()
    page.get_by_role("textbox", name="* First Name").fill("juan")
    page.get_by_role("textbox", name="* Last Name").click()
    page.get_by_role("textbox", name="* Last Name").fill("perez")
    page.get_by_text("First Name Last Name Company").click()
    page.get_by_role("textbox", name="Company").click()
    page.get_by_role("textbox", name="Company").fill("pruebac")
    page.get_by_role("textbox", name="* Address").click()
    page.get_by_role("textbox", name="* Address").fill("arrar 56 \" 15 1")
    page.get_by_role("textbox", name="* City").click()
    page.get_by_role("textbox", name="* City").fill("cali")
    page.get_by_role("textbox", name="* Post Code").click()
    page.get_by_role("textbox", name="* Post Code").fill("70001")
    page.get_by_label("Country").select_option("47")
    page.get_by_label("Region / State").select_option("750")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("checkbox").check()
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Confirm Order").click()
    time.sleep(6)
    page.goto("http://opencart.abstracta.us/index.php?route=checkout/success")
    page.get_by_role("link", name="Continue").click()
