from playwright.sync_api import Page, expect
from pom.home_page_elements import HomePage


def test_home_page(page: Page):
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    home_page = HomePage(page)
    expect(home_page.title_welcome).to_contain_text("Welcome")
    expect(home_page.tomato_icon).to_be_visible()