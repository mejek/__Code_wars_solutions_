# Description:
#
# Due to the popularity of a similar game, a hot new game show has been created and your team has been invited to play!
# The Rules
#
# The game rules are quite simple. The team playing (n players) are lined up at decreasing heights, facing forward such that each player can clearly see all the players in front of them, but none behind.
#
# Red and Blue hats are then placed randomly on the heads of all players, carefully so that a player can not see their own hat. (There may be more Red hats than blue, or vice versa. There might also be no Red, or no Blue hats).
#
# Starting at the back of the line, all players take turns to guess out loud their hat colour. Each team is allowed only one mistake. If two or more players guess the wrong colour, then the game is over and the team loses! But if there is (at most) only one mistake, then they win a huge prize! (All players are on the same team, working together)
#
# There is no communication allowed. If any player tries to say anything (besides their own guess), or tries to turn around, etc. Then that team is immediately disqualified. Play fair!
#
# 1234
#
# In the image above, player 1 sees Blue, Blue, Red, and guesses Blue (wrong!). Then player 2 guesses Blue (correct!). Then player 3 guesses Red (wrong!). Since that was the second mistake, the team loses.
# Task
#
# Your team really wants to win, so you decide to plan a strategy beforehand.
#
# Write a function guess_colour which will be your players strategy to win the game. Each player, when it is their turn, will use this strategy (your function, with the relevant inputs) to determine what their guess will be.
#
# To pass the kata, your function must consistently allow your team to win the game (by the rules explained above). If it causes more than one wrong guess per game, you lose!
#
# Inputs:
#
#     guesses: a list of all previous guesses ("Red" or "Blue") which the player has heard so far (in order).
#     hats: a list of all the hats ("Red" or "Blue") which the player can see in front of them (in order).
#
# Output: the player's guess ("Red" or "Blue").
#
# All inputs will be valid, and length of each list will be between 0 and 999 inclusive. Total size of teams will be between 2 and 1000 inclusive.
#
# Note: the players strategy should not require global variables or state. Tests will check that the strategy is consistent even when called at unexpected times.
#
# Good luck!
#
# My solution:
def guess_colour(guesses, hats):
    if guesses == []:
        if hats.count('Blue') % 2 != 0:
            flag_blue = 1
            return 'Blue'
        else:
            return 'Red'

    else:
        if guesses[0] == 'Blue':
            if guesses.count('Blue') % 2 != 0:
                flag_blue = 1
            else:
                flag_blue = 0
        else:
            if guesses.count('Blue') % 2 != 0:
                flag_blue = 1
            else:
                flag_blue = 0

        if flag_blue == 0:
            if hats.count('Blue') % 2 == 0:
                return 'Red'
            else:
                flag_blue = 1
                return 'Blue'
        else:
            if hats.count('Blue') % 2 == 0:
                flag_blue = 0
                return 'Blue'
            else:
                return 'Red'