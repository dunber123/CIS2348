
lemon = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input("Enter amount of water (in cups):\n"))
agave = float(input("Enter amount of agave nectar (in cups):\n"))
serves = float(input("How many servings does this make?\n"))

print('\nLemonade ingredients - yields','{:.2f}'.format(serves), 'servings')
print('{:.2f}'.format(lemon), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(agave), 'cup(s) agave nectar\n')

serve_req = float(input("How many servings would you like to make?\n"))
print('\nLemonade ingredients - yields', '{:.2f}'.format(serve_req), 'servings')
serv = serve_req/serves
lemon = lemon * serv
water = water * serv
agave = agave * serv
print('{:.2f}'.format(lemon), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(agave), 'cup(s) agave nectar')

print('\nLemonade ingredients - yields', '{:.2f}'.format(serve_req), 'servings')
lemon = lemon / 16
water = water / 16
agave = agave / 16
print('{:.2f}'.format(lemon), 'gallon(s) lemon juice')
print('{:.2f}'.format(water), 'gallon(s) water')
print('{:.2f}'.format(agave), 'gallon(s) agave nectar')
