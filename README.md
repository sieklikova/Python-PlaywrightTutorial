# Python-PlaywrightTutorial

https://branch-blob-4bf.notion.site/Playwright-Framework-d3d07a5e5b0644e09ec0e8962e7af0da

https://playwright.dev/python/docs/test-assertions

https://playwright.dev/python/docs/pom

#používá se, aby se mi test zastavil:  
page.pause()

page.wait_for_load_state("networkidle")

python course
www page for testing:
https://symonstorozhenko.wixsite.com/website-1
pytest ./test/test_1.py --headed --slowmo=1000

automaticky vygeneruje testovací kód na základě tvých akcí v prohlížeči
elementy přes:
playwright codegen https://www.saucedemo.com/

pytest ./test/test_login.py --headed --slowmo=1000

spuštění testů: python test.py

spustit vsechny testy
pytest

spustit jeden soubor:
pytest test_sample.py

spustit jeden test v jednom souboru
pytest test_sample.py::test_answe_two

spustit testy pod tagem
pytest -m sum

LOCATORS
Najít locator v consoli:
playwright.$('xpath=//div[@id="okButton_SM_ROOT_COMP827"]')
nebo
$x("  ")

Pokud chceš jen najít element v běžném prohlížeči, použij klasické JS:

    document.querySelector('#okButton_SM_ROOT_COMP827')
-----------------------------------------------------------------------
Když tedy napíšeme shop_women = ShopWomen(page), děláme toto:

Říkáme Pythonu, aby vytvořil nový, prázdný objekt typu ShopWomen.

Automaticky se zavolá metoda __init__(self, page) v rámci třídy ShopWomen.

Předáme objekt page (který reprezentuje aktuální stránku v prohlížeči, kterou Playwright řídí) do __init__.

Uvnitř __init__ se pak tento page objekt použije k definování a uložení všech selektorů elementů (např. self.shop_women a self.shoes) jako atributů tohoto konkrétního objektu shop_women.

Výsledkem je, že proměnná shop_women teď drží objekt, který má přístup ke všem definovaným elementům stránky "Shop Women", a ty s nimi můžeš snadno interagovat v testu (např. shop_women.shop_women.click() nebo expect(shop_women.shoes).to_be_visible()).

Je to základní kámen pro psaní čistých, udržovatelných a srozumitelných automatizovaných UI testů.
----------------------------------------------------------------------------------------
#GIT

1) create branch: git branch create_test_home_page 
2) git add .; nebo git add nazev_souboru
3) git commit -m "refactoring" // -m je pro psaní zprávy
4) git fetch //synchronizace se vzdáleným repozitářem
5) git push origin ""název branche
