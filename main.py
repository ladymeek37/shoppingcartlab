from customer import Customer
from product import Product

#give customer a name
name = Customer("Lady")

#print customer name
print("Customer name:", name.customer_name)

#create items to be added
rice = Product("Rice", 1.00, "Grains")
chicken = Product("Chicken", 3.00, "Meats")
cucumber = Product("Cucumber", 0.50, "Veggie")

#add items to cart
name.add_item_to_cart(rice)
name.add_item_to_cart(chicken)
name.add_item_to_cart(cucumber)

#see items in cart
name.see_items_in_cart()

#find total 
total = name.cart.calculate_cart_total()
print ("The total for", name.customer_name, "is", total, "!")

#empty car
name.cart.empty_products()
name.see_items_in_cart()


