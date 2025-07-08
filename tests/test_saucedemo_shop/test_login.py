
from playwright.sync_api import Page, expect
import pytest

#vytvorit funkci na login
def login_modul(page:Page, username: str, password: str):
 page.locator("[data-test=\"username\"]").fill(username)
 page.locator("[data-test=\"password\"]").fill(password)
 page.locator("[data-test=\"login-button\"]").click()

#funk která se bude volat automaticky před každým testem. Pro setting se vytvoří f-ce fixture.
@pytest.fixture(autouse=True)
#setting
def befor_and_after_tests(page):
    page.goto("https://www.saucedemo.com/")
# Ve fixture musíme nadefinovat, kde se pouštějí testy
    yield page # dpřidáme page, protože chceme testům dát page
# Testdown, to co se děje po testu např. smazání databáze

def test_correct_login(page:Page):
 #zavoláme f-ci na login
 login_modul(page, "standard_user", "secret_sauce")
 expect(page.get_by_text("Swag Labs"))
#vytvor invalid login

def test_locked_person_login(page:Page):
   #zavoláme f-ci na login
   login_modul(page, "locked_out_user", "secret_sauce")
   expect(page.locator("[data-test=\"error\"]")).to_be_visible()

