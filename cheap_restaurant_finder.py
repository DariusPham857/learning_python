shop1 = {
    "name": "Restaurant 1",
    "location": "Son Tra",
    "menu": [
        {"name": "Water", "type": "drink", "price": 2000 },
        {"name": "Pizza Hai San", "type": "food", "price": 200000 },
        {"name": "Pizza Meat Lovers", "type": "food", "price": 210000 },
        {"name": "Pizza 4 cheese", "type": "food", "price": 220000 },
        {"name": "Pepsi", "type": "drink", "price": 15000 },
        {"name": "Coke", "type": "drink", "price": 15000 },
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
    return find_cheapest_item(shop, "food")

def find_drink_lowest(shop) :
    return find_cheapest_item(shop, "drink")

def find_cheapest_item(shop, item_type):
    cheapest_item = None
    for item in shop["menu"]:
        if  item["type"] == item_type and (cheapest_item is None or item["price"] < cheapest_item):
            cheapest_item = item["price"]
    return cheapest_item


def get_lowest_combo_pershop(shops):
    lowest_combo_per_shop = {}
    for shop in shops:
        lowest_combo_per_shop[shop["name"]] = find_drink_lowest(shop) + find_food_lowest(shop)
    return lowest_combo_per_shop


def filter_by_location(shops, locations):
    allowed_shops = []
    allowed_locations = [x.lower() for x in locations]

    for shop in shops:
        if shop["location"].lower() in allowed_locations:
            allowed_shops.append(shop)
    return allowed_shops


def find_the_lowest(shops, locations):
    allowed_shops = filter_by_location(shops, locations)
    lowest_combo_per_shop = get_lowest_combo_pershop(allowed_shops)

    lowest_price = lowest_combo_per_shop[next(iter(lowest_combo_per_shop))]
    shop_with_lowest_price = None
    for shop, price in lowest_combo_per_shop.items():
        if price < lowest_price:
            lowest_price = price
            shop_with_lowest_price = shop

        
    return shop_with_lowest_price, lowest_price
    


print(find_the_lowest(shops, ["thanh khe", "son TRA", "Lien Chieu"]))



