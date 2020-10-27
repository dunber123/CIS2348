#Rhahan Sarwar
#1818964
#CIS2348 Homework 3 10.11


def printRoster():
    keys = list(players.keys())

    keys.sort()
    print("ROSTER")
    for key in keys:
        print("Jersey number: %d, Rating: %d" % (key, players[key]))


players = {}

for i in range(5):
    jersey_n = int(input("Enter player %d's jersey number:\n" % (i + 1)))
    players[jersey_n] = int(input("Enter player %d's rating:\n" % (i + 1)))
    print("")

printRoster()

while True:
    print(
        "\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n")

    option = input("Choose an option:\n")

    if option == 'o':
        printRoster()

    elif option == 'a':
        jersey_n = int(input("Enter a new player's jersey number:\n"))
        rate = int(input("Enter the player's rating:\n"))
        players[jersey_n] = rate

    elif option == 'd':
        jersey_n = int(input("Enter a player's jersey number:\n"))

        if jersey_n in list(players.keys()):
            del players[jersey_n]

    elif option == 'u':
        jersey_n = int(input("Enter a player's jersey number:\n"))
        rate = int(input("Enter a new rating for player:\n"))
        players[jersey_n] = rate

    elif option == 'r':
        rate = int(input("Enter a rating:\n"))
        keys = list(players.keys())
        keys.sort

        print("\nABOVE %d" % (rate))
        count = 0
        for key in keys:
            if (players[key] > rate):
                print("Jersey number: %d, Rating: %d" % (key, players[key]))
                count += 1
        if (count == 0):
            print("No players found above %d rating" % (rate))

    if option == "q":
        break   