import re
from playwright.sync_api import Page, expect
import pytest

def test_login(page: Page):
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.get_by_test_id("handle-button").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("lekninek@centrum.cz")
    page.get_by_role("textbox", name="Password").fill("lekninek")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    expect(page.get_by_test_id("handle-button")).not_to_contain_text("Log In")






