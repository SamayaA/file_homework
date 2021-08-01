
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



