import random
import string
import json

def get_random_ingredient_name():
    item_names = ["Chicken", "Steak", "Cheese", "Fajitas", "Black Beans", "Pinto Beans", "Rice", "Salsa", "Guacamole", "Sour Cream", "Lettuce", "Tomato", "Onion", "Cilantro", "Jalapeno", "Corn", "Bell Pepper", "Carrot", "Cucumber", "Radish", "Mushroom", "Zucchini", "Spinach", "Kale", "Arugula", "Chard", "Collard Greens", "Mustard Greens", "Turnip Greens", "Beet Greens", "Bok Choy", "Napa Cabbage", "Savoy Cabbage", "Red Cabbage", "Green Cabbage", "Kohlrabi", "Broccoli", "Cauliflower", "Brussels Sprouts", "Asparagus", "Artichoke", "Eggplant", "Okra", "Squash", "Pumpkin", "Sweet Potato", "Yam", "Potato", "Carrot", "Beet", "Radish", "Turnip", "Parsnip", "Rutabaga", "Celery", "Fennel", "Leek", "Scallion", "Shallot", "Garlic", "Ginger", "Turmeric", "Cinnamon", "Nutmeg", "Cloves", "Allspice", "Cardamom", "Coriander", "Cumin", "Paprika", "Chili Powder", "Cayenne", "Black Pepper", "White Pepper", "Pink Pepper", "Green Pepper", "Szechuan Pepper", "Star Anise", "Clove", "Cinnamon", "Nutmeg", "Mace", "Ginger", "Turmeric", "Cardamom", "Coriander", "Cumin", "Paprika", "Chili Powder", "Cayenne", "Black Pepper", "White Pepper", "Pink Pepper", "Green Pepper", "Szechuan Pepper", "Star Anise", "Clove", "Cinnamon", "Nutmeg", "Mace", "Ginger", "Turmeric", "Cardamom", "Coriander", "Cumin", "Paprika", "Chili Powder", "Cayenne", "Black Pepper", "White Pepper", "Pink Pepper", "Green Pepper", "Szechuan Pepper", "Star Anise",]
    return random.choice(item_names)

def create_random_ingredient_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=25))

def make_ingredient(order_id, item_id):
    random_total_ingredients = random.randint(1, 10)
    ingredients = []
    for i in range(1, random_total_ingredients):
        ingredient = {
            "name": get_random_ingredient_name(),
            "id": create_random_ingredient_id(),
            "amountInGrams": random.randint(200, 1000),
        }
        ingredients.append(ingredient)

    order_item_ingredients = {
       "orderId": order_id,
        "itemId": item_id,
       "ingredients": ingredients,      
    }

    return order_item_ingredients

def write_order_obj(order, i):
    with open("order-" + str(i) + ".json", "w") as f:
          json.dump(order, f)


# Opening JSON file
f = open('orders.json')
 
# returns JSON object as 
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
count = 2
for i in data["orders"]:
    orderid = i["orderid"]
    itemid = i["id"]
    payload = make_ingredient(orderid, itemid)
    write_order_obj(payload, count)
    count += 1
 
# Closing file
f.close()