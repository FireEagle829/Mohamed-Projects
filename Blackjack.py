import random as rd
import copy as cp

print()
print("Welcome to Blackjack")
print("By Mohamed Emad")
print()
input("Press Enter to start the game\n")
print()
print("The goal is to reach 20,000$")
print()

player_money = 5000
print("Total Money: {}$".format(player_money))
bet = int(input("Place your bet\n"))
if bet > player_money:
    while True:
        print("You don't have enough money")
        bet = int(input("Place your bet\n"))
        if bet > player_money:
            continue
        else:
            break
player_money -= bet
cards = ["Spades Ace", "Diamonds Ace", "Clubs Ace", "Hearts Ace", "Spades 2", "Diamonds 2", "Clubs 2", "Hearts 2",
         "Spades 3", "Diamonds 3", "Clubs 3", "Hearts 3", "Spades 4", "Diamonds 4", "Clubs 4", "Hearts 4",
         "Spades 5", "Diamonds 5", "Clubs 5", "Hearts 5", "Spades 6", "Diamonds 6", "Clubs 6", "Hearts 6",
         "Spades 7", "Diamonds 7", "Clubs 7", "Hearts 7", "Spades 8", "Diamonds 8", "Clubs 8", "Hearts 8",
         "Spades 9", "Diamonds 9", "Clubs 9", "Hearts 9", "Spades 10", "Diamonds 10", "Clubs 10", "Hearts 10",
         "Spades King", "Diamonds King", "Clubs King", "Hearts King", "Spades Queen", "Diamonds Queen", "Clubs Queen",
         "Hearts Queen",
         "Spades Jack", "Diamonds Jack", "Clubs Jack", "Hearts Jack"]
rd.shuffle(cards)
cards_copy = cp.copy(cards)

player_points = 0
player_cards = None
dealer_points = 0
dealer_cards = None
player_statement = None
dealer_statement = None
ace1 = None
ace2 = None
ace3 = None
ace4 = None
flag = 0
flag_2 = 0
flag_3 = 0
dealer_cards_copy = None


def player_first_draw():
    global player_cards, player_statement, ace1, ace2
    player_cards = rd.sample(cards, 2)
    cards.remove(player_cards[0])
    cards.remove(player_cards[1])
    if "Ace" in player_cards[0] and "Ace" in player_cards[1]:
        player_first_draw()
    player_statement = "You got {} and {} as starting cards".format(player_cards[0], player_cards[1])
    print(player_statement)
    print()
    if player_statement.count("Ace") == 1:
        print("You got an Ace, Would you like it to be a 1 or 11?\n")
        ace1 = int(input("Enter 1 for 1 or 2 for 11\n"))
    elif player_statement.count("Aces") == 1:
        print("You got 2 Aces, Would you like the first one to be a 1 or 11?\n")
        ace1 = int(input("Enter 1 for 1 or 2 for 11\n"))
        print()
        print("Would you like the second one to be a 1 or 11?\n")
        ace2 = int(input("Enter 1 for 1 or 2 for 11\n"))
        print()
    else:
        pass


def dealer_first_draw():
    global dealer_cards, dealer_statement, dealer_points, ace3, ace4, dealer_cards_copy
    dealer_cards = rd.sample(cards, 2)
    dealer_cards_copy = cp.copy(dealer_cards)
    cards.remove(dealer_cards[0])
    if "Ace" in dealer_cards[0] and "Ace" in dealer_cards[1]:
        dealer_first_draw()
    dealer_statement = "You got {} and {} as starting cards".format(dealer_cards[0], dealer_cards[1])
    if dealer_statement.count("Ace") == 1:
        ace3 = rd.sample([1, 2], 1)
    elif dealer_statement.count("Aces") == 1:
        ace3 = rd.sample([1, 2], 1)
        ace4 = rd.sample([1, 2], 1)
    else:
        pass


player_first_draw()
dealer_first_draw()


def player_first_points_transformation(element):
    global player_points
    name = element.split(" ")[1]
    if name == "Jack" or name == "Queen" or name == "King":
        player_points += 10
    elif name == "Ace":
        if ace1 == 1:
            player_points += 1
        elif ace1 == 2:
            player_points += 11
        if ace2 == 1:
            player_points += 1
        elif ace2 == 2:
            player_points += 11
        else:
            pass
    else:
        player_points += int(name)


def dealer_first_point_transformation(element):
    global dealer_points
    name = element.split(" ")[1]
    if name == "Jack" or name == "Queen" or name == "King":
        dealer_points += 10
    elif name == "Ace":
        if ace1 == 1:
            dealer_points += 1
        elif ace1 == 2:
            dealer_points += 11
        if ace2 == 1:
            dealer_points += 1
        elif ace2 == 2:
            dealer_points += 11
        else:
            pass
    else:
        dealer_points += int(name)


dealer_first_point_transformation(dealer_cards[0])
dealer_first_point_transformation(dealer_cards[1])
player_first_points_transformation(player_cards[0])
player_first_points_transformation(player_cards[1])
print("You now have {} points".format(str(player_points)))

print("Pick a card to reveal\n")

while True:
    player_revealed_card = str(input("\n"))
    if player_revealed_card.title() not in player_cards:
        print("Please enter a card you have!")
    else:
        break
print()
print("Card revealed!")
print()
dealer_revealed_card = rd.sample(dealer_cards, 1)
print("Dealer has revealed {}".format(dealer_revealed_card[0]))
print()
dealer_cards_copy.remove(dealer_revealed_card[0])


def player_draw():
    global player_points, player_cards, player_money, flag
    card = rd.sample(cards, 1)[0]
    cards.remove(card)
    print("You got {}".format(card))
    print()
    if "Ace" in card:
        print("You got an ace, Would you like it to be a 1 or 11?")
        ace = int(input("Enter 1 for 1 or 2 for 11\n"))
        print()
    else:
        ace = None
    player_cards.append(card)
    name = card.split(" ")[1]
    if name == "Jack" or name == "Queen" or name == "King":
        player_points += 10
    elif name == "Ace":
        if ace == 1:
            player_points += 1
        elif ace == 2:
            player_points += 11
        else:
            pass
    else:
        player_points += int(name)
    if player_points > 21:
        print("You lost the round")
        print("Your points were greater than 21 ({})".format(player_points))
        print()
        print("Total Money: {}$".format(player_money))
        print()
        if player_money == 0:
            print()
            print("You lost the game...")
            print("Better luck next time :DD")
            print()
            input("Press Enter to quit\n")
            quit()

        flag = 1


def stand():
    global flag_2, dealer_points, dealer_cards, player_points, flag_3, cards, player_money
    points_2 = 0
    print()
    print("The dealer has revealed {} as his second card".format(dealer_cards_copy[0]))
    print()
    card = rd.sample(cards, 1)[0]
    cards.remove(card)
    name = card.split(" ")[1]
    if name == "Jack" or name == "Queen" or name == "King":
        points_1 = 10
    elif name == "Ace":
        points_1 = 1
        points_2 = 11
        flag_2 = 1
    else:
        points_1 = int(name)

    if (dealer_points + points_1) <= 21 and flag_2 == 0:
        dealer_cards.append(card)
        dealer_points += points_1

    elif (dealer_points + points_1) <= 21 and flag_2 == 1:
        if (dealer_points + points_2) < (dealer_points + points_1) <= 21:
            dealer_cards.append(card)
            dealer_points += points_1
        elif (dealer_points + points_1) < (dealer_points + points_2) <= 21:
            dealer_cards.append(card)
            dealer_points += points_2
    else:

        pass
    if player_points > dealer_points:
        player_money += 2*bet
        print()
        print("You won the round!")
        print()
        print("Dealer's cards: ")
        print(dealer_cards)
        print("Your points: {}".format(player_points))
        print("Dealer's points: {}".format(dealer_points))
        print("Your money: {}".format(player_money))
        flag_3 = 1
    elif player_points == dealer_points:
        player_money += bet
        print("Round is draw")
        print()
        print("Dealer's cards:")
        print(dealer_cards)
        print("Dealer's points: {}".format(dealer_points))
        print("Your points: {}".format(player_points))
        print()
        print("Your money: {}".format(player_money))
        flag_3 = 1
    else:
        print("You lost the round!")
        print()
        print("Dealer's cards: ")
        print(dealer_cards)
        print("Dealer's points: {}".format(dealer_points))
        print("Your points: {}".format(player_points))
        print("Your money: {}".format(player_money))
        flag_3 = 1


while True:
    print()
    print("Hit or Stand?")
    print()
    option = str(input("\n"))
    if option.lower() == "hit":
        player_draw()
    elif option.lower() == "stand":
        stand()
    else:
        print("Please enter a valid option")
    if flag == 0 and flag_3 == 0:
        continue
    else:
        break
if player_money == 0:
    print()
    print("You lost the game...")
    print("Better luck next time :DD")
    print()
    x = input("Press Enter to quit\n")
    quit()


while True:
    print()
    print("Next Round!")
    print()
    cards = cards_copy
    print()
    print("Total Money: {}$".format(player_money))
    bet = int(input("Place your bet\n"))
    if bet > player_money:
        while True:
            print("You don't have enough money")
            bet = int(input("Place your bet\n"))
            if bet > player_money:
                continue
            else:
                break
    player_money -= bet
    rd.shuffle(cards)
    cards_copy = cp.copy(cards)
    player_points = 0
    player_cards = None
    dealer_points = 0
    dealer_cards = None
    player_statement = None
    dealer_statement = None
    ace1 = None
    ace2 = None
    ace3 = None
    ace4 = None
    flag = 0
    flag_2 = 0
    flag_3 = 0
    dealer_cards_copy = None
    player_first_draw()
    dealer_first_draw()
    dealer_first_point_transformation(dealer_cards[0])
    dealer_first_point_transformation(dealer_cards[1])
    player_first_points_transformation(player_cards[0])
    player_first_points_transformation(player_cards[1])
    print("You now have {} points".format(str(player_points)))
    print("Pick a card to reveal\n")
    while True:
        player_revealed_card = str(input("\n"))
        if player_revealed_card.title() not in player_cards:
            print("Please enter a card you have!")
        else:
            break
    print()
    print("Card revealed!")
    print()
    dealer_revealed_card = rd.sample(dealer_cards, 1)
    print("Dealer has revealed {}".format(dealer_revealed_card[0]))
    print()
    dealer_cards_copy.remove(dealer_revealed_card[0])
    while True:
        print()
        print("Hit or Stand?")
        print()
        option = str(input("\n"))
        if option.lower() == "hit":
            player_draw()
        elif option.lower() == "stand":
            stand()
        else:
            print("Please enter a valid option")
        if flag == 0 and flag_3 == 0:
            continue
        else:
            break
    if player_money >= 20000:
        print()
        print("You won the game!")
        print()
        print("Well Done! :DDD")
        break
    elif player_money == 0:
        print()
        print("You lost the game..")
        print()
        print("Better luck next time :DD")
        break

input("Press Enter to exit")


## A game completely made by Mohamed Emad in 3 hours :D

