from shopping_cart import ShoppingCart

class Customer:
    def __init__(self, name):
        self.customer_name = name
        self.cart = ShoppingCart()

    def add_item_to_cart(self, product):
        self.cart.add_products_to_cart(product)
        print (self.customer_name, "added", product.name, "to their cart" )

    def see_items_in_cart(self):
        print ("Items in cart:")
        for product in self.cart.products:
            print (product.name)

