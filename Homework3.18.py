wall_h = int(input("Enter wall height (feet):\n"))
wall_w = int(input("Enter wall width (feet):\n"))
colors = {'red': 35, 'blue': 25, 'green': 23}
wall_a = wall_h * wall_w
gal_paint = wall_a / 350
can = round(gal_paint)

print("Wall area:", wall_a, "square feet")
print("Paint needed:", '{:.2f}'.format(gal_paint), "gallons")
print("Cans needed:", can, "can(s)")


color_selection = input('\nChoose a color to paint the wall:\n')
if color_selection in colors:
    costs = colors[color_selection]
    totalcost = costs * can
    print('Cost of purchasing', color_selection, 'paint:', '$%d' % (totalcost))