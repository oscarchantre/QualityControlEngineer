import pytest
import time
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.password import ResetPass
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import os
import uuid

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False, 
        "slow_mo": 3000      
    }

VIDEO_DIR = "videos"

# Configuración del contexto para guardar videos
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        "ignore_https_errors": True,
        "record_video_dir": VIDEO_DIR   #  carpeta donde se guardan videos
    }


# Parametrización del correo
def generate_email():
    unique_id = uuid.uuid4().hex[:6]  # 6 caracteres aleatorios
    return f"juancarlos{unique_id}@yopmail.com"
@pytest.mark.parametrize("email", [generate_email()])


def test_opencart(page: Page, email):
    home = HomePage(page)
    register = RegisterPage(page)
    account = ResetPass(page)
    product = ProductPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    home.open()
    home.go_to_register()
    register.fill_registration_form("Juan", "Perez", email, "123457890", "123457890")
    time.sleep(3)
    account.reset_password("123456789")

    product.add_macbook_pro_to_cart()
    home.search_product("Samsung Galaxy")
    product.add_search_result_to_cart()

    cart.open_cart()
    cart.remove_macbook()
    product.add_search_result_to_cart()
    cart.open_cart()
    cart.view_cart()

    page.get_by_role("link", name="Checkout", exact=True).click()
    checkout.fill_checkout_form(
        "juan", "perez", "Empresa de Prueba",
        "Carrera Siempre viva 12 # 13 - 80", "cali",
        "70001", "47", "750"
    )
    # Guardar el video al terminar
    video = page.video
    page.close()
    if video:
        video_path = video.path()
        new_name = os.path.join(VIDEO_DIR, f"{test_opencart.__name__}.mp4")
        video.save_as(new_name)
        print(f"Video guardado en: {new_name}")
