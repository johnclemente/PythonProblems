import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_cards():
    return [random.choice(cards), random.choice(cards)]

def decide_winner(player_cards, dealer_cards):
    player_total = sum(player_cards)
    dealer_total = sum(dealer_cards)
    
    # show results
    print("\nyour hand:")
    for i in range(len(player_cards)):
        print (player_cards[i])
    print("\ndealer hand:")
    for i in range(len(dealer_cards)):
        print (dealer_cards[i])
    print(f"\nYour total: {player_total}")
    print(f"dealer total: {dealer_total}")
    
    # evaluate
    if (player_total <= dealer_total or player_total > 21):
        print("you lost")
    else: print("you win!")
    

# clear input and add condition to check for mistypes
def player_choice(player_cards, dealer_cards):
    decision = ""
    while decision not in ["y", "n"]:
        decision = input("\nenter 'y' to get another card, enter 'n' to stay: ") 
        if (decision == "n"):
            decide_winner(player_cards, dealer_cards)
            break
        if (decision == "y"):
            add_card(player_cards, dealer_cards)
            break
        else: print("hmmm looks like you hit the wrong key, try again!")
    
def add_card(player_cards, dealer_cards):
    new_card = random.choice(cards)
    player_cards.append(new_card)
    print(f"\nyour new card is {new_card}")
    # check for bust
    if (sum(player_cards) > 21):
        print("you busted!")
        decide_winner(player_cards, dealer_cards)
    else: player_choice(player_cards, dealer_cards)


def play():
    deal_cards()
    player_cards = deal_cards()
    dealer_cards = deal_cards()
    print(f"your cards are: {player_cards[0]} and {player_cards[1]}")
    print(f"house cards are: {dealer_cards[0]} and ?")
    player_choice(player_cards, dealer_cards)

play()

