import random

suits = ('clubs', 'diamonds', 'hearts', 'spades')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'king', 'queen', 'ace')
#card_value = ('two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'jack':10, 'king':10, 'queen':10):

class Cards:
    def __init__ (self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + 'of' + self.suit
    
    def value(self):
        if self.rank in ['jack', 'king', 'queen']:
            return 10
        elif self.rank == 'ace':
            return 1,11
        else:
            return int(self.rank)

class Deck:
    def __init__(self):
        self.cards = []
        for rank in ranks:
            for suit in suits:
                c = Cards(rank,suit)
                self.cards.append(c)
                
    def shuffle(self):
        random.shuffle(self.cards)
        
    def draw(self):
        print(f'Here is self.cards before the problematic line: {self.cards}')
        if not self.cards:
            raise Exception("deck empty")
        card = self.cards.pop()
        return card
    
    def __str__(self):
        cards = []
        for c in self.cards:
            cards.append(str(c))
        return str(cards)
    
class Player:
    def __init__(self):
        self.hand = []
        self.blackjack = False
        self.bust = False
        self.stand = False

    def turn(self, deck):
        hit_options = ["HIT", "Hit", "hit"]
        stand_options = ["STAND", "Stand", "stand"]
        while(self.stand == False) and (self.bust == False) and (self.blackjack == False):
            hit_or_stand = input("Hit or Stand?: \n")
            if hit_or_stand in hit_options:
                self.rank.append(deck)
                self.ace_check()
                self.blackjack_check()
                print("Your current hand is:")
                self.showHand()
            elif hit_or_stand in stand_options:
                self.stand = True
                break
            else:
                print(f"'{hit_or_stand}' is not a valid response.")

    #def draw(self, deck):
        #self.hand.append(deck.drawCard())

    def showhand(self):
        for card in self.hand:
            card.show_card()
        player_hand_total_check = []
        for card in self.hand:
            player_hand_total_check.append(card.face_value)
        play_hand_total1 = sum(player_hand_total_check)
        print(f"The total of the hand is: {play_hand_total1}")

    def ace_adjust(self):
        hand_ace_adjust_list = []
        number_of_cards_in_hand = len(self.hand)
        for card in self.hand:
            hand_ace_adjust_list.append(card.face_value)
        hand_total = sum(hand_ace_adjust_list)
        if 11 in hand_ace_adjust_list and hand_total > 21:
            count = 0
            for card in self.hand:
                if card.face_value == 11:
                    card.face_value = 1
                if hand_ace_adjust_list[count] == 11:
                    hand_ace_adjust_list[count] = 1
                if sum(hand_ace_adjust_list) <= 21:
                    break
                count += 1

    def blackjack_check(self):
        hand_list = []
        for card in self.hand:
            hand_list.append(card.face_value)
        if sum(hand_list) == 21:
            self.blackjack = True
            print("BLACKJACK")
        elif sum(hand_list) > 21:
            self.bust = True

class Dealer(Player):
    def __init__(self):
        super().__init__()

    #def show_initial_hand(self):
        #self.hand[0].show_card()
        #print(f"The value of the Dealer's face-up card is: {self.hand[0].face_value}")

    def dealer_turn(self, deck):
        check_list_17 = []
        for card in self.hand:
            check_list_17.append(card.face_value)
        while sum(check_list_17) < 17:
            self.draw(deck)
            self.ace_check()
            self.blackjack_check()
            check_list_17.append(self.hand[-1].face_value)
        print("Dealer hand: ")
        self.showhand()
    
      
class Human(Player):
    def __init__(self):
        super().__init__()

    def show_initial_hand(self):
        self.hand[0].show_card()
        print(f"Your cards are: {self.hand[0].face_value}")

    def human_turn(self, deck):
        check_list = []
        for card in self.hand:
            check_list.append(card.face_value)
        self.showhand()
    
class Game:
    def __init__(self, main='I am the coolest main ever'):
        self.main = main
        self.games = 0
        self.main_game_loop = True
        self.player = Player()
        self.dealer = Dealer()
        self.first_turn_new_game = False
        self.turns = False
    
        def main(self):
            self.main

    def games(self):
        self.choice = input("Would you like to play BlackJack? Yes or No" )
        print(self.choice)
        
    def run(self):
        while self.main_game_loop == True:
            deck = Deck()
            deck.shuffle()             
            #self.deal_cards(deck)
            print("Your Hand:")
            self.player.blackjack_check()
            self.player.showhand()
            print("Dealer's hand:")
            self.dealer.blackjack_check()
            self.compare_first_hand()
            if(self.first_turn_new_game == True):
                self.another_game()
            else:
                self.player.turn(deck)
                self.dealer.dealer_turn(deck)
                self.compare_hands()
                self.another_game()

    #def deal_cards(self, deck):
        #for i in range(0, 2):
            #self.player.draw(deck)
            #self.dealer.draw(deck)
        #self.player.ace_check()
        #self.dealer.ace_check()

    def compare_first_hand(self):
        if (self.player.blackjack == True) and (self.dealer.blackjack == True):
            self.dealer.showHand()
            self.player.ties += 1
            self.dealer.ties += 1
            print("The game is a tie!")           
            self.first_turn_new_game = True
        elif (self.player.blackjack == True) and (self.dealer.blackjack == False):
            self.dealer.showHand()
            self.player.wins += 1
            self.dealer.losses += 1
            print("You win!")
            self.first_turn_new_game = True
        elif (self.player.blackjack == False) and (self.dealer.blackjack == True):
            self.dealer.showHand()
            self.player.losses += 1
            self.dealer.wins += 1
            print("You lost!")
            self.first_turn_new_game = True

        else:
            self.turns = True
            self.dealer.showhand()

    def compare_hands(self):
        if (self.player.blackjack == True) and (self.dealer.blackjack == True):
            self.player.ties += 1
            self.dealer.ties += 1
            print("The game is a tie!")
        elif (self.player.blackjack == True) and (self.dealer.bust == False) and (self.dealer.blackjack == False):
            self.player.wins += 1
            self.dealer.losses += 1
            print("You win!")
        elif (self.player.bust == True) and (self.dealer.blackjack == True):
            self.player.losses += 1
            self.dealer.wins += 1
            print("You lost!")  
        elif (self.player.bust == True):
            self.player.losses += 1
            self.dealer.wins += 1
            print("You lost!")
        elif (self.dealer.bust == True) and (self.player.bust == False) and (self.player.blackjack == False):
            self.player.wins += 1
            self.dealer.losses += 1
            print("You win!")
        else:
            player_hand = []
            dealer_hand = []
            for card in self.player.hand:
                player_hand.append(card.face_value)
            for card in self.dealer.hand:
                dealer_hand.append(card.face_value)
            if sum(player_hand) > sum(dealer_hand):
                self.player.wins += 1
                self.dealer.losses += 1
                print("You win!")
            elif sum(player_hand) == sum(dealer_hand):
                self.player.ties += 1
                self.dealer.ties += 1
                print("The game is a tie!")           
            elif sum(player_hand) < sum(dealer_hand):
                self.player.losses += 1
                self.dealer.wins += 1
                print("You lost!")
        

    def final_results(self):
        print("Final results:")
        print("Your wins: {} | Your losses: {} Ties {}".format(self.player.wins, self.player.losses, self.player.ties))
        print("Thank's for playing!")

    def another_game(self):
        while(True):
            play_again_yes_options = ["Yes"]
            play_again_no_options = ["No"]
            play_again = input("Would you like to play again? Yes or No: ")
            if play_again in play_again_yes_options:
                self.reset_variables()
                break
            elif play_again in play_again_no_options:
                self.final_results()
                self.main_game_loop = False
                break
            else:
                print(f"{play_again} is not a valid response.")
                
my_game = Game()

print(my_game)
print(my_game.main)

my_game.run()