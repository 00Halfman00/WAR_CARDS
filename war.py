
# Card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle
import os

############################################################################
############################   CLASSES     #################################
############################################################################

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    SUITS = 'H D S C'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self):
        self.deck = []
        self.card_suits = []


    def create_deck(self):
        """
        For each suite, each member in the ranks is combined with it as a tupple to the deck.
        It also creates a list of cards for each suite and appends them to a list.
        """
        suits = None
        for i, suit in enumerate(self.SUITS):
            suits = []
            for j, rank in enumerate(self.RANKS):
                self.deck.append((suit, rank))
                suits.append((suit, rank))
            self.card_suits.append(suits)


    def shuffle_deck(self):
        """
        Shuffles the deck of cards
        """
        shuffle(self.deck)


    def split_deck(self):
        """
        Checks if deck has been created first. If so, splits deck in two,
        shuffles each and returns them
        """
        return (self.deck[:26], self.deck[26:])


    def print_deck(self):
        if len(self.card_suits):
            for i, suit in enumerate(self.card_suits):
                print(suit)


################################################################################
################################################################################
################################################################################
################################################################################


class Hand():
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def remove_card(self, card):
        self.hand.remove(card)

    def __str__(self) -> str:
        return f" {len(self.hand)} cards."

################################################################################
################################################################################
################################################################################
################################################################################

class Player(Hand):
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class.
    """
    def __init__(self):
        self.hand = []
    def __init__(self, name):
        self.name = name



#############################################################################################
################################# HELPER FUNCTIONS ##########################################
#############################################################################################


def get_players():
    """
    returns a tuple with two strings
    """
    name_one = ''
    name_two = ''
    while not len(name_one):
        name_one = input("\nPlayer 1, enter the name by which you wish to raise war with:   ")
    while not len(name_two):
        name_two = input("\nPlayer 2, enter the name by which you wish to raise war with:   ")
    return (name_one, name_two)


def get_deck():
    """
    creates a Deck class instance, creates a deck of cards, prints all the cards in their respective
    suit, shuffles cards, and returns a tupple with two list of 26 cards each.
    """
    deck = Deck()
    deck.create_deck();
    print('\tThese are the cards that we will be using: \n')
    deck.print_deck()
    print('\n\tNow let me shuffle them quickly so that we can start the game.\n\n')
    deck.shuffle_deck();
    halves = deck.split_deck()
    return halves


def print_board(first_player, second_player):
    """
    prints the first card in each players hand
    """
    print("PlayerOne's card:\n")
    print(first_player.hand[0])
    print("number of cards: " + str(len(first_player.hand)))
    print("\n\nPlayerTwo's card:\n")
    print(second_player.hand[0])
    print("number of cards: " + str(len(second_player.hand)))


def print_tie_board(first_player, second_player):
    """
    prints three upside down cards and one turned up card for each player
    """
    while True:
        if len(first_player.hand) > 4 and len(second_player.hand) > 4:
            print("PlayerOne's cards:\n\n")
            print([(' ', ' '), (' ', ' '), (' ', ' '), first_player.hand[4]])
            print("number of cards: " + str(len(first_player.hand)))
            print("\n\nPlayerTwo's cards:\n\n")
            print("number of cards: " + str(len(second_player.hand)))
            print([(' ', ' '), (' ', ' '), (' ', ' '), second_player.hand[4]])
            break
        else:
            if len(first_player.hand) > len(second_player.hand):
                print("Player One wins the game!")
            else:
                print('Player Two wins the game')
            break


def get_highest_rank(one, two):
    """
    returns True if player one has the higher ranking card, else it returns False
    """
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'
    return RANKS.index(one) > RANKS.index(two)


def adjust_one_card(first_player, second_player, is_true):
    """
    if is_true is True, player_one won the round, else player_two won the round
    function that wil remove a card from the player's hand that lost
    and add it to the player's hand that won
    """
    card_won = ""
    if(is_true):
        card_won = second_player.hand[0]
        second_player.remove_card(card_won)
        first_player.add_card(first_player.hand.pop(0))
        first_player.add_card(card_won)
    else:
        card_won = first_player.hand[0]
        first_player.remove_card(card_won)
        second_player.add_card(second_player.hand.pop(0))
        second_player.add_card(card_won)


def get_five(hands, is_true):
    """
    if is_true is True, player_one won the round, else player_two won the round
    take five cards from the player that lost and add them to the winning player's cards
    """
    while True:
        if len(hands[0]) >= 5 and len(hands[1]) >= 5:
            for i, (player_one_card, player_two_card) in enumerate(zip(*hands)):
                if i == 5:
                    break
                if is_true:
                    hands[0].append(player_two_card)
                    hands[1].remove(player_two_card)
                else:
                    hands[1].append(player_one_card)
                    hands[0].remove(player_one_card)
            break
        else:
            if len(hands[0]) > len(hands[1]):
                print("Player One wins the game!")
            else:
                print('Player Two wins the game')
            break



def second_tie_war(first_player, second_player):
    """
    loops while both players cards are equal
    breaks when a winner is found and adjust both players hands
    """
    count = 4
    while(first_player.hand[count][1] == second_player.hand[count][1]):
        count += 2
        if len(first_player.hand) >= count and len(second_player.hand) >= count:
            if first_player.hand[count][1] != second_player.hand[count][1]:
                first_wins = get_highest_rank(first_player.hand[count][1], second_player.hand[count][1])
                if first_wins:
                    print('\nwinning card: ',first_player.hand[count][1])
                else:
                    print('\nwinning card: ', second_player.hand[count][1])
                adjust_many((first_player.hand, second_player.hand), first_wins, count)
        else:
            if len(first_player.hand) > len(second_player.hand):
                print("Player One wins the game!")
            else:
                print('Player Two wins the game')
            break

def adjust_many(hands, is_true, count):
    """
    if is_true is True, player_one won the round, else player_two won the round
    take as many cards as represented by count from the player that lost
    and add them to the winning player's cards
    """
    for i, (player_one_card, player_two_card) in enumerate(zip(*hands)):
        if i == count:
            break
        if is_true:
            hands[0].append(player_two_card)
            hands[1].remove(player_two_card)
        else:
            hands[1].append(player_one_card)
            hands[0].remove(player_one_card)


def check_winner(first_player, second_player):
    """
    returns true if either of both players has no cards left
    """
    if(not len(first_player.hand) or not len(second_player.hand)):
        return True
    else:
        return False


######################
#### GAME PLAY #######
######################


def start_war_game():
    """
    introduces itself, gets players names, creates players instance,  creates running environment, ,
    """
    print('\n\n\tWelcome to the game of WAR!! I will be your host and dealer for the game.\n\n')

    players = get_players()
    player_one = Player(players[0])
    player_two = Player(players[1])
    os.system('clear')
    halves = get_deck()
    player_one.hand = halves[0]
    player_two.hand = halves[1]

    # run time for game
    while True:
        #############################################################################################
        # announcements and print playerOne's card and playerTwo's card
        #############################################################################################
        response1 = input("Players, are you ready to move...\n\n")
        print_board(player_one, player_two)
        response2 = input('\n\npress enter to see who won the round  ')


        #############################################################################################
        #  check to see if there is a tie
        #############################################################################################
        if(player_one.hand[0][1] == player_two.hand[0][1]):
            response3 = input("\n\nWhat?........... It's a tie. Press enter to start Tie Breaker War")
            os.system('clear')

            # check to see if each player has enough cards to play tie war
            if len(player_one.hand) > 4 and len(player_two.hand) > 4:
                print_tie_board(player_one, player_two)

                #check to see if there is a tie again
                if player_one.hand[4][1] == player_two.hand[4][1]:
                    second_tie_war(player_one, player_two)

                # if not a tie again, get round winner and adjust player's cards
                else:
                    one_wins = get_highest_rank(player_one.hand[4][1], player_two.hand[4][1])
                    if(one_wins):
                        print('\nwinning card: ',player_one.hand[4])
                    else: print('\nwinning card: ', player_two.hand[4])
                    get_five((player_one.hand, player_two.hand), one_wins)

            # if not enough cards to play tie war, announce winner
            else:
                if len(player_one.hand) > len(player_two.hand):
                    print('PlayerOne has won the WAR')
                else:
                    print('PlayerTwo has won the WAR')
                break


        #############################################################################################
        # if not a tie, check for winner and adjust cards
        #############################################################################################
        else:
            one_wins = get_highest_rank(player_one.hand[0][1], player_two.hand[0][1])
            if one_wins:
                print('\nwinning card: ',player_one.hand[0])
            else:
                print('\nwinning card: ', player_two.hand[0])
            adjust_one_card(player_one, player_two, one_wins)


        #############################################################################################
        # check for a winner by seeing who still has cards
        #############################################################################################
        if check_winner(player_one, player_two):
            if len(player_one.hand):
                print('PlayerOne has won the WAR')
            else:
                print('PlayerTwo has won the WAR')
            break

        response4 = input('press enter to play next round:   ')
        os.system('clear')
    print('Thanks for playing WAR')



####################################################################################
################################ PLAY GAME #########################################
####################################################################################


start_war_game()

