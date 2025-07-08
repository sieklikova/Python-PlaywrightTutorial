
class HomePage:
    # init method, default argument page, tato třída slouží jako reprezentace domovské stránky
    def __init__(self, page):
        self.tomato_icon = page.get_by_role("link", name="pomidor.png")
        self.title_welcome = page.locator("h1")


