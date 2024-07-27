class User
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.orders = []

    def set_password(self, password):
        self.password = password

    def check_password(self, password):
        return self.password == password

class FoodItem:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class OrderItem:
    def __init__(self, food_item, quantity):
        self.food_item = food_item
        self.quantity = quantity

class Order:
    def __init__(self, user):
        self.user = user
        self.items = []
        self.status = "Pending"

    def add_item(self, food_item, quantity):
        self.items.append(OrderItem(food_item, quantity))

    def update_item(self, food_item, quantity):
        for item in self.items:
            if item.food_item.id == food_item.id:
                if quantity == 0:
                    self.items.remove(item)
                else:
                    item.quantity = quantity
                break

    def total_price(self):
        return sum(item.food_item.price * item.quantity for item in self.items)

    def place_order(self):
        self.status = "Placed"
        self.user.orders.append(self)

    def order_status(self):
        return self.status
