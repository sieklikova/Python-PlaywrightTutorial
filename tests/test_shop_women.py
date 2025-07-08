from playwright.sync_api import Page, expect
from pom.shop_women_elements import ShopWomen


def test_shop_women_page(page: Page):
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
   # podrobné vysvětlení v read me
    # Create an instance of the ShopWomen Page Object. ce. Voláš jméno třídy (ShopWomen) jako funkci, a tím Pythonu říkáš: "Vytvoř mi nový objekt podle plánu ShopWomen.
    shop_women = ShopWomen(page)
    # Click on the 'shop_women' locator *inside* the shop_women object
    shop_women.shop_women.click()
    expect(shop_women.shoes).to_be_visible()





