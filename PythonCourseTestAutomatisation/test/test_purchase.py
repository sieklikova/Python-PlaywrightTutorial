
from playwright.sync_api import Page, expect
import pytest

#vytvorit funkci na login
def login_modul(page:Page, username: str, password: str):
    page.locator("[data-test=\"username\"]").fill(username)
    page.locator("[data-test=\"password\"]").fill(password)
    page.locator("[data-test=\"login-button\"]").click()

def check_item_price(page: Page, product_name: str, product_price: str):
    product = (page.locator("[data-test=\"inventory-list\"]")).filter(has_text=product_name)
    expect(product).to_contain_text(product_price)
    return product

def add_to_cart(page: Page, product_slug: str):
    selector = f"[data-test='add-to-cart-{product_slug}']"
    page.locator(selector).click()
    expect(page.locator(f"[data-test=\"remove-{product_slug}\"]")).to_contain_text("Remove")

#funk která se bude volat automaticky před každým testem. Pro setting se vytvoří f-ce fixture. Setting = fixture.
@pytest.fixture(autouse=True)
def befor_and_after_tests(page):
    page.goto("https://www.saucedemo.com/")
    # Ve fixture musíme nadefinovat, kde se pouštějí testy
    yield page # přidáme page, protože chceme testům dát page

#parametrizace produktů = opakovaný stejný test s různými vstupy
@pytest.mark.parametrize("product_name, product_price, product_slug",  [
    ("Sauce Labs Onesie", "$7.99", "sauce-labs-onesie"),
    ("Sauce Labs Fleece Jacket", "$49.99", "sauce-labs-fleece-jacket")
])

def test_purchase_one_item(page:Page, product_name, product_price, product_slug):
    # přihlášení
    login_modul(page, "standard_user", "secret_sauce")
    expect(page.get_by_text("Swag Labs")).to_be_visible()

    #ověření ceny produktu
    check_item_price(page,product_name,product_price)

    #přidání do košíku
    add_to_cart(page, product_slug)

    #kontrola v košíku
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(page.get_by_text(product_name)).to_be_visible()

    page.locator("[data-test=\"checkout\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("hdajsd")
    page.locator("[data-test=\"lastName\"]").fill("dsadsa")
    page.locator("[data-test=\"postalCode\"]").fill("76312")
    page.locator("[data-test=\"continue\"]").click()
    page.locator("[data-test=\"finish\"]").click()
    expect(page.locator("[data-test=\"complete-header\"]")).to_contain_text("Thank you for your order!")

@pytest.mark.parametrize("product_name, product_price, product_slug",  [
    ("Sauce Labs Onesie", "$7.99", "sauce-labs-onesie"),
    ("Sauce Labs Fleece Jacket", "$49.99", "sauce-labs-fleece-jacket")
])
#definování testu, který pracuje s webovou stránkou pomocí objektu page a používá parametry pro prduct_name, product_price, product_slug
def test_purchase_multiple_items(page:Page, product_name, product_price, product_slug):
    login_modul(page, "standard_user", "secret_sauce")
    expect(page.get_by_text("Swag Labs")).to_be_visible()
    #ověření ceny produktu
    check_item_price(page, product_name, product_name)
    # Ručně zadáš slugy – tedy část, která je v data-test atributu
    add_to_cart(page, product_slug)
    # Proceed to checkout. Vytvořit f-ci.

    #kontrola v košíku
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(page.get_by_text(product_name)).to_be_visible()

    page.locator("[data-test='shopping-cart-link']").click()
    expect(page.get_by_text(product_name)).to_be_visible()

    page.locator("[data-test='checkout']").click()
    page.locator("[data-test='firstName']").fill("Alice")
    page.locator("[data-test='lastName']").fill("Smith")
    page.locator("[data-test='postalCode']").fill("11111")
    page.locator("[data-test='continue']").click()
    page.locator("[data-test='finish']").click()
    expect(page.locator("[data-test='complete-header']")).to_contain_text("Thank you for your order!")