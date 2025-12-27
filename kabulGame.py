import random

print(f"Rules of the game:\tYou get 4 cards and you want to get rid of as many of them and get the lowest possible number.\ncards Joker, 1-5 are do nothing except for their value, with joker being 0.\n6-Q each have special moves. K is worth 13 but the king of diamonds and the king of hearts is worth -1")
global turn
global deck
deck = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♥', '2♥', '3♥', '4♥', '5♥','6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣','A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'Joker', 'Joker']
turn = -1
global playerhand
playerhand = []
global kabul
kabul = False


def gameover():
   global playerhand
   global computerhand
   playervalue = 0
   computervalue = 0
   detectable_cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "Joker", "K"]

   # Code that counts the values for player's hand
   for i in range(len(playerhand)):
       detected_card = next((card for card in detectable_cards if card in playerhand[i]), None)
       if any(card in playerhand[i] for card in ["A", "J", "Q", "Joker", "K"]):
           if detected_card == "A":
               playervalue += 1
           elif detected_card == "J":
               playervalue += 11
           elif detected_card == "Q":
               playervalue += 12
           elif detected_card == "Joker":
               playervalue += 0
           elif playerhand[i] in ["K♦", "K♥"]:
               playervalue -= 1
           elif playerhand[i] in ["K♠", "K♣"]:
               playervalue += 13
           else:
               print("error")
       else:
           playervalue += int(detected_card)

   # Code that counts the values for computer's hand
   for i in range(len(computerhand)):
       detected_card = next((card for card in detectable_cards if card in computerhand[i]), None)
       if any(card in computerhand[i] for card in ["A", "J", "Q", "Joker", "K"]):
           if detected_card == "A":
               computervalue += 1
           elif detected_card == "J":
               computervalue += 11
           elif detected_card == "Q":
               computervalue += 12
           elif detected_card == "Joker":
               computervalue += 0
           elif computerhand[i] in ["K♦", "K♥"]:
               computervalue -= 1
           elif computerhand[i] in ["K♠", "K♣"]:
               computervalue += 13
           else:
               print("error")
       else:
           computervalue += int(detected_card)

   print(f"Your hand was {playerhand}")
   print(f"Your value is {playervalue}")
   print(f"Computer's hand was {computerhand}")
   print(f"Computer's value is {computervalue}")

   if computervalue > playervalue:
       print("YOU WON!!!!")
   elif computervalue == playervalue:
       print("Tie")
   else:
       print("COMPUTER WON!!!!")
def playcard():
   global turn
   global kabul
   turn += 1
   cardinpile = [random.choice(deck)]
   deck.remove(cardinpile[0])
   if turn % 2:
       print(f"\ncomputer turn\n")
       compval = cardinpile[0]
       detectable_cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "Joker", "K"]
       detected_card = next((card for card in detectable_cards if card in compval), None)
       if any(card in compval for card in ["A", "2", "3", "4", "5", "Joker", "K"]) and "10" not in compval:
           print("keep the card 1")

           #if computerhand
       else:
           print("put down card")


   else:
       print(f"\nthe card is {cardinpile}\n")
       playerInput = input("1. Swap card, 2. Put card down: \t")
       if playerInput == "1":
           newinput = input("which card position do you want to swap. 0-3:\t")
           playerhand[int(newinput)] = cardinpile[0]
           #print(playerhand)
           print("operation done")
       if playerInput == "2":
           tempval = cardinpile[0]
           character = "1"
           if any(card in tempval for card in ["A", "2", "3", "4", "5", "Joker", "K"]) and "10" not in tempval:
               detectable_cards = ["A", "2", "3", "4", "5", "Joker", "K"]
               detected_card = next((card for card in detectable_cards if card in tempval), None)
               #print("1-5, Joker, or King is in it")
               #detectable_cards = ["1", "2", "3", "4", "5", "Joker", "K"]
               #detected_card = next((card for card in detectable_cards if card in tempval), None)
               if detected_card:
                   #print(f"{detected_card} is in tempval")
                   cardinhand = next((card for card in playerhand if card.startswith(detected_card)), None)
                   if cardinhand:
                       playerhand.remove(cardinhand)
                       print(f"You have a {detected_card} in your hand.")
                       print("Card removed from player's hand:", cardinhand)
                       #print("Player's hand after removing the card:", playerhand)
           else:
               detectable_cards = ["6", "7", "8", "9", "10", "J", "Q"]
               detected_card = next((card for card in detectable_cards if card in tempval), None)
               #print("card placed down is a 6-Q")
               print(detected_card)
               if detected_card in ["6", "7"]:
                   #print("6 or 7")
                   powerupinput = input("choose which card of yours you would like to look at (0-3):\t")
                   print(playerhand[int(powerupinput)])
                   print("done")
               if detected_card in ["8", "9"]:
                   #print("8 or 9")
                   powerupinput = input("choose which card of the computers you would like to look at (0-3):\t")
                   print(computerhand[int(powerupinput)])
                   print("done")
               if detected_card in ["10", "J"]:
                   #print("10 or J")
                   firstcardinput = input("first card to swap (0-3):\t ")
                   secondcardinput = input("second card to swap (0-3):\t ")
                   computerhand[int(firstcardinput)], computerhand[int(secondcardinput)] = computerhand[int(secondcardinput)], computerhand[int(firstcardinput)]
                   #print(computerhand)
                   print("done")
               if detected_card == "Q":
                   #print("Q") - debug
                   powerupinput = input("How many of your cards do you want to look at?:\t")
                   playerhandnum = int(powerupinput)
                   computerhandnum = 2 - playerhandnum

                   for i in range(playerhandnum):
                       powerupinput = input("Which card from your hand? (0-3):\t")
                       print(playerhand[int(powerupinput)])

                   for i in range(computerhandnum):
                       powerupinput = input("Which card from the computer's hand? (0-3):\t")
                       print(computerhand[int(powerupinput)])
                       newinput = input("Do you want this card (y/n):\t")
                       if newinput == "y":
                           newinput = input("Which card do you want to swap from yours? (0-3):\t")
                           playerhand.append(computerhand[int(powerupinput)])
                           computerhand.remove(computerhand[int(powerupinput)])
                           computerhand.append(playerhand[int(newinput)])
                           playerhand.remove(playerhand[int(newinput)])
                   print("done")
       checkDone = input("Do you want to call kabul? (y/n): ")
       if checkDone == "y":
           kabul = True
           print("kabul called!")
       else:
           print("game continue")

               #print(playerhand) - debug
               #print(computerhand) - debug
       #if any(card in cardinpile for card in ["1", "2", "3", "4", "5", "Joker", "K"]):

def playGame():
   global deck
   global playerhand
   global computerhand
   global kabul
   #deck = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♥', '2♥', '3♥', '4♥', '5♥','6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣','A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'Joker', 'Joker']
   repNum = 0
   playerhand = []
   computerhand = []
   while repNum < 4:
       playerhand.append(random.choice(deck))
       deck.remove(playerhand[repNum])
       repNum += 1
   repNum = 0
   while repNum < 4:
       computerhand.append(random.choice(deck))
       deck.remove(computerhand[repNum])
       repNum += 1
   print("your turn")
   print(f"your hand is {playerhand[0]}, {playerhand[1]}")
   print("Computers hand is currently unknown.")
   #print(playerhand)
   #print(computerhand)
   #print(deck)

   #discardpile = []
   while kabul == False:
       playcard()
   gameover()
#gameover()
playGame()