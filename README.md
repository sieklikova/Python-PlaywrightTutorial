# Python-PlaywrightTutorial

https://branch-blob-4bf.notion.site/Playwright-Framework-d3d07a5e5b0644e09ec0e8962e7af0da

https://playwright.dev/python/docs/test-assertions

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
