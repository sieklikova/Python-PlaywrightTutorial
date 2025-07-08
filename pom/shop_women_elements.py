
class ShopWomen:
    def __init__(self, page):
        self.shop_women = page.get_by_role("link", name="Shop Women", exact=True)
        self.shoes = page.get_by_label("Shoes gallery").get_by_role("link", name="Quick View")
        self.lipstick = page.get_by_label("Lipstick gallery").get_by_role("link", name="Quick View")
        self.button_up_t_shirt = page.get_by_role("link", name="Best Seller Quick View")
        self.cool_watch = page.get_by_label("Cool watch gallery").get_by_role("link", name="Quick View")
        self.lotion = page.get_by_role("link", name="New Quick View")
        self.backpack = page.get_by_label("Backpack gallery").get_by_role("link", name="Quick View")
        self.product_85 = page.get_by_role("listitem").filter(has_text="Quick View I'm a productPrice$85.00").get_by_role("link").first
        self.product_40 = page.get_by_role("listitem").filter(has_text="Quick View I'm a productPrice$40.00").get_by_role("link").first
        self.product_130 = page.get_by_role("listitem").filter(has_text="Quick View I'm a productPrice$130.00").get_by_role("link").first
        self.product_45 = page.get_by_role("listitem").filter(has_text="Quick View I'm a productPrice$45.00").get_by_role("link").first
        self.product_95 = page.get_by_role("link", name="Sale Quick View")
        self.product_120 = page.get_by_role("listitem").filter(has_text="Quick View I'm a productPrice$120.00").get_by_role("link").first
        self.profile_icon = page.get_by_test_id("handle-button")
        self.cart_icon = page.get_by_role("button")
