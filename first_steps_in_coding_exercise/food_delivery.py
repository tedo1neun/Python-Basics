amount_chicken_menu = int(input())
amount_fish_menu = int(input())
amount_veg_menu = int(input())

chicken_menu_price = amount_chicken_menu * 10.35
fish_menu_price = amount_fish_menu * 12.40
amount_veg_menu = amount_veg_menu * 8.15

total_main_food = chicken_menu_price + fish_menu_price + amount_veg_menu
desert_price = total_main_food * 20/100
deliver = 2.50

total_price = total_main_food + desert_price + deliver
print(total_price)
