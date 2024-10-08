text = """from bartender import drinkmaker

drink = drinkmaker.make_drink(drink="Bloody Mary", ice=True, double=True)

robot.run(drink)

"""

change = {
    '\n': "{Enter}\nSleep, 700\n",
    ' ': "{Space}\nSleep, 700\n",
}

with open('script.txt', 'w') as f:
    f.write("^>::\n")
    for char in text:
        f.write("Send, ")
        f.write(change[char] if char in change else char)
        f.write('\nSleep, 200\n')
    f.write('return')
        
