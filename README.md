# Three-Nought-Four
A game of three-nought-four (304) I am developing. A text-based card game to which I will add more features as I learn.

This card game uses cards Ace, 7, 8, 9, 10, Jack, Queen, and King.
It is a trick-based game, where each trick has points according to the cards in it. 
The Jack and 9 are promoted above the ace, in the Netherlands Jass style.
As such, Jack = 30 pts, 9 = 20 pts, Ace = 11 pts, 10 = 10 pts (somewhat obviously ^v^), King = 3 pts, Queen = 2 pts, and 7 and 8 do not hold points.

After the first deal of four cards each, players bid for the number of points they will win to get the choice of trump card.

The highest bidder gets to choose a trump card, and play begins.

Each player, starting from the player to the left of the dealer (assumed to be the human player for simplicity in this code) plays a single card, and the others must follow suit whenever possible.

If no cards of the suit remain in a players hand, they may either cut the trick by passing a trump, or they may pass a card of any suit.

At the end of play, the bidders win if they achieve their bid + 100 points, and the others win if they do not.

This implementation is a simpler "open trump" version where everyone knows the trump from the beginning. 
I will implement the traditional closed trump version as I go further in this project.


## To Run:
Just download the code, and run the python file.
As of now, this is a text based game running in the terminal, but I am learning front end, and hope to add a GUI soon!
Enjoy!!!

(Additionally, the bots are playing mostly randomly, so if you know the game, you should be able to win most of the time, 
Given, of course, that lady luck (-ahem- python's random library) smiles upon you)
