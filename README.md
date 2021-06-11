# Overview

This is a digital version of the card based game Uno that follows the MVC (Model, View, Controller) programming pattern.

The game consists primarily of cards with both a colour and a number. Each player starts with a deck of seven cards.
The player whose cards are visible is the starting player. Once the player makes a move by selecting their card to play,
their cards will be hidden and it will move to the next player's turn.

There are two piles in the middle of the board. The left pile is the pickup pile, a player should click this pile if they have no cards to play,
it will add a card to their deck. The right pile is the putdown pile, a player has to pick a card from their deck which matches the card on top of the putdown pile.

The aim of the game is to have no cards left in your deck. Each turn a player can either select a card from their pile which matches the card
on top of the putdown pile, or they can pick up a new card from the pickup pile if they have no matching cards.
