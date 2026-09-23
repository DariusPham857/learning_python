shop1 = {
    "name": "Restaurant 1",
    "location": "Son Tra",
    "menu": [
        {"name": "Pizza Hai San", "type": "food", "price": 200000 },
        {"name": "Pizza Meat Lovers", "type": "food", "price": 210000 },
        {"name": "Pizza 4 cheese", "type": "food", "price": 220000 },
        {"name": "Pepsi", "type": "drink", "price": 15000 },
        {"name": "Coke", "type": "drink", "price": 15000 },
        {"name": "Water", "type": "drink", "price": 15000 },
    ]
}

# 1. A traditional Vietnamese Pho restaurant
shop2 = {
    "name": "Pho Ba Diem",
    "location": "Hai Chau",
    "menu": [
        {"name": "Pho Bo (Beef Noodle Soup)", "type": "food", "price": 50000},
        {"name": "Pho Ga (Chicken Noodle Soup)", "type": "food", "price": 45000},
        {"name": "Goi Cuon (Spring Rolls)", "type": "food", "price": 30000},
        {"name": "Tra Da (Iced Tea)", "type": "drink", "price": 5000},
        {"name": "Cafe Sua Da (Iced Milk Coffee)", "type": "drink", "price": 20000}
    ]
}

# 2. A popular coffee and boba shop
shop3 = {
    "name": "The Highland Cafe",
    "location": "Thanh Khe",
    "menu": [
        {"name": "Banh Mi Thit", "type": "food", "price": 25000},
        {"name": "Phin Sua Da", "type": "drink", "price": 29000},
        {"name": "Tra Sen Vang (Lotus Tea)", "type": "drink", "price": 45000},
        {"name": "Matcha Freeze", "type": "drink", "price": 55000},
        {"name": "Brown Sugar Boba", "type": "drink", "price": 40000}
    ]
}

# 3. A Western-style burger joint
shop4 = {
    "name": "Burger Bros",
    "location": "Ngu Hanh Son",
    "menu": [
        {"name": "Classic Cheeseburger", "type": "food", "price": 90000},
        {"name": "Double Bacon Burger", "type": "food", "price": 130000},
        {"name": "French Fries", "type": "food", "price": 40000},
        {"name": "Coca Cola", "type": "drink", "price": 20000},
        {"name": "Vanilla Milkshake", "type": "drink", "price": 60000}
    ]
}

# 4. A healthy vegan eatery
shop5 = {
    "name": "Green Leaf Vegan",
    "location": "Lien Chieu",
    "menu": [
        {"name": "Vegan Pad Thai", "type": "food", "price": 65000},
        {"name": "Mushroom Hotpot", "type": "food", "price": 150000},
        {"name": "Tofu Salad", "type": "food", "price": 45000},
        {"name": "Fruit Kombucha", "type": "drink", "price": 45000},
        {"name": "Fresh Coconut Water", "type": "drink", "price": 25000}
    ]
}

# 5. A local beachfront seafood restaurant
shop6 = {
    "name": "Hai San Bien Dong",
    "location": "Son Tra",
    "menu": [
        {"name": "Grilled Octopus", "type": "food", "price": 120000},
        {"name": "Steamed Clams with Lemongrass", "type": "food", "price": 80000},
        {"name": "Lobster with Garlic Butter", "type": "food", "price": 550000},
        {"name": "Tiger Beer", "type": "drink", "price": 25000},
        {"name": "Heineken Beer", "type": "drink", "price": 30000}
    ]
}

lowest_overall = None

# Combine them all into a single list
shops = [shop1, shop2, shop3, shop4, shop5, shop6]
def find_food_lowest(shop) :
    lowest_in_current_shop = None
    for item in shop["menu"]:
        if lowest_in_current_shop is None:
            lowest_in_current_shop = item["price"]
        if item["type"] == "food" and item["price"] < lowest_in_current_shop:
            lowest_in_current_shop = item["price"]
    return lowest_in_current_shop

lowest_in_shop1 = find_food_lowest(shop1)

if lowest_overall is None:
    lowest_overall = lowest_in_shop1
if lowest_in_shop1 < lowest_overall:
    lowest_overall = lowest_in_shop1
