import pytest
from main import User, FoodItem, Order, OrderItem

def test_user_creation():
    user = User("testuser", "password123")
    assert user.username == "testuser"
    assert user.check_password("password123")
    assert not user.check_password("wrongpassword")

def test_user_set_password():
    user = User("testuser", "password123")
    user.set_password("newpassword")
    assert user.check_password("newpassword")
    assert not user.check_password("password123")

def test_food_item_creation():
    item = FoodItem(1, "Burger", 5.99)
    assert item.id == 1
    assert item.name == "Burger"
    assert item.price == 5.99

def test_order_add_item():
    user = User("testuser", "password123")
    item1 = FoodItem(1, "Burger", 5.99)
    order = Order(user)
    order.add_item(item1, 2)
    assert len(order.items) == 1
    assert order.items[0].food_item == item1
    assert order.items[0].quantity == 2

def test_order_update_item():
    user = User("testuser", "password123")
    item1 = FoodItem(1, "Burger", 5.99)
    item2 = FoodItem(2, "Fries", 2.99)
    order = Order(user)
    order.add_item(item1, 2)
    order.add_item(item2, 3)
    order.update_item(item2, 1)
    assert len(order.items) == 2
    assert order.items[1].quantity == 1

def test_order_update_item_remove():
    user = User("testuser", "password123")
    item1 = FoodItem(1, "Burger", 5.99)
    item2 = FoodItem(2, "Fries", 2.99)
    order = Order(user)
    order.add_item(item1, 2)
    order.add_item(item2, 3)
    order.update_item(item1, 0)
    assert len(order.items) == 1
    assert order.items[0].food_item == item2

def test_order_total_price():
    user = User("testuser", "password123")
    item1 = FoodItem(1, "Burger", 5.99)
    item2 = FoodItem(2, "Fries", 2.99)
    order = Order(user)
    order.add_item(item1, 2)
    order.add_item(item2, 3)
    assert order.total_price() == pytest.approx(20.95, 0.01)

def test_order_place_order():
    user = User("testuser", "password123")
    item1 = FoodItem(1, "Burger", 5.99)
    order = Order(user)
    order.add_item(item1, 2)
    order.place_order()
    assert order.order_status() == "Placed"
    assert len(user.orders) == 1
    assert user.orders[0] == order

def test_order_item_quantity():
    user = User("testuser", "password123")
    item1 = FoodItem(1, "Burger", 5.99)
    order = Order(user)
    order.add_item(item1, 5)
    assert order.items[0].quantity == 5

def test_order_empty_order():
    user = User("testuser", "password123")
    order = Order(user)
    assert order.total_price() == 0
    assert len(order.items) == 0
    order.place_order()
    assert order.order_status() == "Placed"
    assert len(user.orders) == 1
    assert user.orders[0] == order

# Run the tests with pytest
if __name__ == "__main__":
    pytest.main()
