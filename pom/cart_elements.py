class cart:
    def __init__(self, page):
      self.view_cart = page.get_by_role("button", name="View Cart")
      self.delete_icon = page.get_by_role("button", name="remove Lipstick from the cart")