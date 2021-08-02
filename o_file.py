
from pprint import pprint

with open('data.txt' , 'r', encoding="UTF8") as file :
    cook_book = dict()
    for line in file:
        dish = line.strip()
        cook_book[dish] = []
        amount_ingredients = int(file.readline())
        for i in range (amount_ingredients) :
            line = ((file.readline().strip()).split(' | '))
            cook_book[dish].append(dict())
            cook_book[dish][i]['ingredient_name'] = line[0]
            cook_book[dish][i]['quantity'] = int(line[1])
            cook_book[dish][i]['measure'] = line[2]
        file.readline()
 
def get_shop_list_by_dishes(dishes, person_count):
	ingredients = dict()
	for i in range(0 , len(dishes)):
		dish_ingredients = cook_book.get(dishes[i])
		for j in range(0 , len (dish_ingredients)):
			ingredient_name = dish_ingredients[j]['ingredient_name']
			if (ingredients.get(ingredient_name) == None):
				ingredients[ingredient_name] = dict()
				ingredients[ingredient_name]['measure'] = dish_ingredients[j]['measure']
				ingredients[ingredient_name]['quantity'] = dish_ingredients[j]['quantity']
			ingredients[ingredient_name]['quantity'] += dish_ingredients[j]['quantity']
	return ingredients
				
