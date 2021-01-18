import random


class Card:
    """
    The basic number, colour and methods of a UNO card
    """
    def __init__(self, number, colour):
        """
        Construct a card based on its number and colour.
        :param number (int): The number of the card
        :param colour (str): The colour of the card
        """
        self._number = number
        self._colour = colour

    def __str__(self):
        """
        Return the string representation of the card.
        :return (str): The string representation of the card
        """
        return "Card({}, {})".format(self._number, self._colour)

    __repr__ = __str__

    def get_number(self):
        """
        Return the number of the card.
        :return (int): The number of the card
        """
        return self._number

    def get_colour(self):
        """
        Return the colour of the card.
        :return (str): The colour of the card
        """
        return self._colour

    def set_number(self, number):
        """
        Set the number of the card.
        :param number: (int) The number of the card
        """
        self._number = number

    def set_colour(self, colour):
        """
        Set the colour of the card.
        :param colour: (str) The colour of the card
        """
        self._colour = colour

    def get_pickup_amount(self):
        """
        Return the amount of cards the next player should pick up.
        :return (int): The amount of cards the next player should pick up
        """
        return 0

    def matches(self, card):
        """
        Determine if the next card is to be placed on the pile matches this card.
        :param card: Another instance of the Card class
        :return (bool): True if the cards match with each other in number or colour and false otherwise
        """
        return self._number == card.get_number() or self._colour == card.get_colour()

    def play(self, player, game):
        """
        No special action
        :param player: An instance of the Player class or its subclasses
        :param game: An instance of the UnoGame class from uno_util.py
        """
        pass


class SkipCard(Card):
    """
    A card which skips the turn of the next player.
    """
    def __str__(self):
        """
        Return the string representation of the skip card.
        :return (str): the string representation of the skip card
        """
        return "SkipCard({}, {})".format(self.get_number(), self.get_colour())

    __repr__ = __str__

    def play(self, player, game):
        """
        Skip the turn of the next player
        :param player: An instance of the Player class
        :param game: An instance of the UnoGame class from uno_util.py
        """
        game.skip()

    def matches(self, card):
        """
        Determine if the next card is to be placed on the pile matches this card.
        :param card: Another instance of the Card class
        :return (bool): True if the cards match with each other in colour and false otherwise
        """
        return self.get_colour() == card.get_colour()


class ReverseCard(Card):
    """
    A card which reverses the order of turns.
    """
    def __str__(self):
        """
        Return the string representation of the reverse card.
        :return (str): The string representation of the reverse card
        """
        return "ReverseCard({}, {})".format(self.get_number(), self.get_colour())

    __repr__ = __str__

    def play(self, player, game):
        """
        Reverse the order of turns.
        :param player: An instance of the Player class
        :param game: An instance of the UnoGame class from uno_util.py
        """
        game.reverse()

    def matches(self, card):
        """
        Determine if the next card is to be placed on the pile matches this card.
        :param card: Another instance of the Card class
        :return (bool): True if the cards match with each other in colour and false otherwise
        """
        return self.get_colour() == card.get_colour()


class Pickup2Card(Card):
    """
    A card which makes the next player pick up two cards
    """
    def __str__(self):
        """
        Return the string representation of the Pickup2 card.
        :return (str): The string representation of the Pickup2 card
        """
        return "Pickup2Card({}, {})".format(self.get_number(), self.get_colour())

    __repr__ = __str__

    def matches(self, card):
        """
        Determine if the next card is to be placed on the pile matches this card.
        :param card: Another instance of the Card class
        :return (bool): True if the cards match with each other in colour and false otherwise
        """
        return self.get_colour() == card.get_colour()

    def get_pickup_amount(self):
        """
        Return the amount of cards the next player should pick up.
        :return (int): The amount of cards the next player should pick up
        """
        return 2

    def play(self, player, game):
        """
        Make the next player pick up two cards.
        :param player: An instance of the Player class
        :param game: An instance of the UnoGame class from uno_util.py
        """
        next_player_deck = game.get_turns().peak().get_deck()  # Get the next player's deck of cards.
        pickup_cards = game.pickup_pile.pick(self.get_pickup_amount())  # Get the cards that need to be picked up.
        next_player_deck.add_cards(pickup_cards)  # Add the cards to the next player's deck of cards


class Pickup4Card(Card):
    """
    A card which makes the next player pick up four cards
    """
    def __str__(self):
        """
        Return the string representation of the Pickup4 card.
        :return (str): The string representation of the Pickup4 card
        """
        return "Pickup4Card({}, {})".format(self.get_number(), self.get_colour())

    __repr__ = __str__

    def matches(self, card):
        """
        Determine if the next card is to be placed on the pile matches this card.
        :param card: Another instance of the Card class
        :return (bool): True if the cards match with each other in colour and false otherwise
        """
        return True

    def get_pickup_amount(self):
        """
        Return the amount of cards the next player should pick up.
        :return (int): The amount of cards the next player should pick up
        """
        return 4

    def play(self, player, game):
        """
        Make the next player pick up four cards.
        :param player: An instance of the Player class
        :param game: An instance of the UnoGame class from uno_util.py
        """
        next_player_deck = game.get_turns().peak().get_deck()  # Get the next player's deck of cards.
        pickup_cards = game.pickup_pile.pick(self.get_pickup_amount())  # Get the cards that need to be picked up.
        next_player_deck.add_cards(pickup_cards)  # Add the cards to the next player's deck of cards


class Deck:
    """
    A collection of ordered Uno cards
    """
    def __init__(self, starting_cards=None):
        """
        Construct a deck of cards.
        :param starting_cards (list<Card>): The starting deck of cards
        """
        if starting_cards is None:
            starting_cards = []
        self._starting_cards = starting_cards

    def get_cards(self):
        """
        Return the deck of cards.
        :return (list<Card>): The deck of cards
        """
        return self._starting_cards

    def get_amount(self):
        """
        Return the amount of cards in the deck.
        :return (int): The amount of cards in the deck
        """
        return len(self._starting_cards)

    def shuffle(self):
        """
        Shuffle the order of the cards in the deck.
        """
        random.shuffle(self._starting_cards)

    def pick(self, amount=1):
        """
        Take the first 'amount' of cards off the deck and return them.
        :param amount: The amount of cards to be picked
        :return (list<Card>): The first 'amount' of cards
        """
        result = []
        for _ in range(amount):
            popped_card = self._starting_cards.pop()
            result.append(popped_card)
        return result

    def add_card(self, card):
        """
        Place a card on top of the deck.
        :param card: An instance of the Card class
        """
        self._starting_cards.append(card)

    def add_cards(self, cards):
        """
        Place a list of cards on top of the deck.
        :param cards: (list<Card>) A list of cards
        """
        self._starting_cards.extend(cards)

    def top(self):
        """
        Peaks at the card on top of the deck and returns it or None if the deck is empty.
        :return: The card on top of the deck or None if the deck is empty
        """
        if self._starting_cards:
            return self._starting_cards[-1]
        return None


class Player:
    """
    A representation of one of the players in a game of uno
    """
    def __init__(self, name):
        """
        Construct a player in a game.
        :param name (str): The name of the player
        """
        self._name = name
        self._deck = Deck()

    def get_name(self):
        """
        Return the name of the player.
        :return: The name of the player
        """
        return self._name

    def get_deck(self):
        """
        Return the player's deck of cards.
        :return: The player's deck of cards
        """
        return self._deck

    def is_playable(self):
        """
        Raise a NotImplementedError on the base Player class.
        """
        raise NotImplementedError("is_playable to be implemented by subclasses")

    def has_won(self):
        """
        Return True if the player has an empty deck and therefore won.
        :return: True the player has won
        """
        if not self._deck.get_cards():
            return True
        return False

    def pick_card(self, putdown_pile):
        """
        Raise a NotImplementedError on the base Player class.
        :param putdown_pile: An instance of the Deck class
        """
        raise NotImplementedError()


class HumanPlayer(Player):
    def is_playable(self):
        """
        Return True if the player's moves aren't automatic.
        :return: True if the player's moves aren't automatic.
        """
        return True

    def pick_card(self, putdown_pile):
        """
        Selects a card to play from the players current deck.
        :param putdown_pile: An instance of the Deck class
        :return: None for non-automated players
        """
        return None


class ComputerPlayer(Player):
    def is_playable(self):
        """
        Return True if the player's moves aren't automatic.
        :return: True if the player's moves aren't automatic.
        """
        return False

    def pick_card(self, putdown_pile):
        """
        Selects a card to play from the players current deck.
        :param putdown_pile: An instance of the Deck class
        :return: The matching card if it can be found.
        """
        for card in self.get_deck().get_cards():
            if card.matches(putdown_pile.top()):
                self.get_deck().get_cards().remove(card)
                return card


def main():
    # Import uno_util here if you wish to execute command lines to test the code
    """
    Please refer to gui.py
    """
    print("Please run gui.py instead")


if __name__ == "__main__":
    main()
