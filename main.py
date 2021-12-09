
import random
game = input("Do you want to play blackjack game? type 'yes' or 'no'")
from art import logo

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  random1 = random.choice(cards)
  return random1


def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
    if 11 in cards and sum(cards) >21:
      cards.remove(11)
      cards.append(1)

  return sum(cards)



def compare(user_score, com_score):
  if user_score == com_score:
    return "draw"
  elif com_score == 0:
    return "lose, opponent has blackjack"
  elif user_score == 0:
    return "won, you have a blackjack"
  elif com_score >21:
    return "won, computer exceeds the limit"
  elif user_score>21:
    return "lose, you exceeds the limit"
  elif user_score>com_score:
    return "you won"
  elif com_score>user_score:
    return "you lost"
def continue_game(): 
  print(logo) 
  user_cards = []
  computer_cards = []
  game_over = False
  for i in range(2):
    new_card = deal_card()
    user_cards.append(new_card)
    computer_cards.append(new_card)

  while not game_over:

    user_score = calculate_score(user_cards)
    com_score = calculate_score(computer_cards)
    print(f"your cards are {user_cards} and total score is: {user_score}")
    print(f"computer first card is {computer_cards[0]}")
    if user_score == 0 and com_score == 0 and user_score > 21:
      game_over = True
    else:
      more_card = input ("do you want to draw another? type 'yes' or 'no'")
      if more_card == 'yes':
        user_cards.append(deal_card())
      else:
        game_over = True

    while com_score != 0 and com_score<17:
      computer_cards.append(deal_card())
      com_score = calculate_score(computer_cards)

  print(f"your cards are {user_cards} and total score is: {user_score}")
  print(f"computer first card is {computer_cards} and computer final score is: {com_score}")
  print(compare(user_score,com_score))

while input("do u want to continue the game? type 'yes' or 'no'") == "yes":
  continue_game()
  