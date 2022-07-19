print ("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
""")
appetizers = ['Wings', 'Cookies', 'Spring Rolls']
entrees = ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden']
desserts = ['Ice Cream', 'Cake', 'Pie']
drinks = ['Coffee', 'Tea', 'Unicorn Tears']

print("""
Appetizers
----------
""")
for appetizer in appetizers:
    print(appetizer)

print("""
Entrees
----------
""")
for entree in entrees:
    print(entree)

print("""
Desserts
----------
""")
for dessert in desserts:
    print(dessert)

print("""
Drinks
----------
""")
for drink in drinks:
    print(drink)

print("""
***********************************
** What would you like to order? **
***********************************
""")

items = {}

while True:
    order = input("> ").lower()
    single_order = 'order'
    big_order = 'orders'
    if order == 'quit':
        break


    if items.get(order):
        items[order] += 1
        big_order = big_order
    else:
        items[order] = 1
        single_order = single_order

    if items[order] > 1:
        big_order = big_order
    else:
        big_order = single_order

#    if items[order]:
#       items[order] = 1
#
#   elif items[order] > 1:
#      big_order = big_order
# else:
#    big_order = single_order
    print(f"** {items[order]} {big_order} of {order} have been added to your meal**")




