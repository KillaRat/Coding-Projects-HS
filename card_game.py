##########################
'''
Using the Python Turtle Deck of Cards project, create any card game that uses the
deck_of_cards and player_cards lists and the draw_card() functions.
Ideas include Game of War, Go Fish, or Blackjack. Extra credit will be given for more complicated projects
such as Uno, Hearts, Spoons, etc.
Your project should append and remove items from the deck_of_cards and player_cards lists depending on the game.
Your program should call the draw_card() function as appropriate for your game.
You need to include a game over (win or lose) to your card game and a play again feature.
Your program must include your own function (definitions with parameters and calls with arguments).

'''
########################
import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("green")
screen.title("Deck of Cards")

# Initialize turtles
t = turtle.Turtle()
t.speed(0)
t2 = turtle.Turtle()
t2.speed(0)

# Card ranks and suits
rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["♠", "♥", "♦", "♣"]
color = ["red", "black"]
deck = []


# Function to randomize colors (for card color)
def rc():
    return random.randint(0, 1)


# Function to calculate the hand value in Blackjack
def value(lst):
    val = 0
    ace_count = 0  # Count how many Aces are in hand
    for thing in lst:
        if thing[0] == "A":
            val += 11
            ace_count += 1
        elif thing[0] in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            val += int(thing[0])
        elif thing[0] in ["J", "Q", "K"]:
            val += 10

    # Adjust for Aces if value exceeds 21
    while val > 21 and ace_count:
        val -= 10
        ace_count -= 1

    return val


# Create the deck
for r in rank:
    for s in suits:
        deck.append((r, s))


# Function to draw a card
def draw_card(t, x, y, w, h, color, suit, rank):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.color("white")
    t.setheading(0)
    for _ in range(2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
    t.end_fill()
    t.penup()
    t.goto(x + 5, y - 25)
    t.pendown()
    t.color(color)
    t.write(rank, font=("Times New Roman", 16, "normal"))
    t.penup()
    t.goto(x + 5, y - 45)
    t.pendown()
    t.write(suit, font=("Times New Roman", 16, "normal"))
    t.penup()
    t.goto(x + (w - 20), y - (h - 20))
    t.pendown()
    t.color(color)
    t.write(suit, font=("Times New Roman", 16, "normal"))
    t.penup()
    t.goto(x + (w - 19), y - h)
    t.pendown()
    t.write(rank, font=("Times New Roman", 16, "normal"))


# Deal two cards to each player
def deal_initial_cards():
    player1 = []
    player2 = []
    for _ in range(2):
        card = deck.pop(random.randrange(len(deck)))
        player1.append(card)
        card = deck.pop(random.randrange(len(deck)))
        player2.append(card)
    return player1, player2


# Draw the initial hand for each player
def display_player1_cards(player1):
    x, y = -50, 50
    for card in player1:
        draw_card(t, x, y, 85, 170, color[rc()], card[1], card[0])
        x += 100  # Move next card to the right


def player2_cards(player2):
    x, y = -50, 250
    for card in player2:
        draw_card(t, x, y, 85, 170, color[rc()], card[1], card[0])
        x += 100  # Move next card to the right


# Function to ask player whether to draw a card
def draw_for_player(player_hand):
    card = deck.pop(random.randrange(len(deck)))
    player_hand.append(card)
    return card


# Player 1's turn
def player1_turn(player1):

    p1_val = 0
    # While Player 1 hasn't busted and wants to draw
    while p1_val<=21:  # Player can only draw if they haven't busted
        p1_val = value(player1)
        print(f"Player 1 hand: {player1} Value: {p1_val}")
        action = input("Player 1: Would you like to draw a card? (yes/no): ").lower()

        #if action == "yes":
        while True:
            if p1_val >= 21:
                return p1_val
            if action in ["Yes", "yes", "Y", "y"]:
                new_card = draw_for_player(player1)
                print("Player 1 drew:", new_card)
                display_player1_cards(player1)
                p1_val = value(player1)
                print(p1_val)
                if p1_val>21:
                    return p1_val
                #return p1_val
                action = input("Player 1: Would you like to draw a card? (yes/no): ").lower()
                # Recalculate value after drawing
            elif action in  ["no", "No", "N", "n"]:
                return p1_val
            else:
                print("Invalid input. Please type 'yes' or 'no'.")
                break

    #return p1_val

    # Check if Player 1 busted
    '''if not still_in_game or p1_val > 21:
        print(f"Player 1's hand value: {p1_val} - Player 1 busts!")
        return p1_val  # Return the busted value to check in main game loop
    return p1_val
'''

# Player 2's turn (same as before, except we check if Player 1 busted)
def player2_turn(player2):
    p2_val = value(player2)
    while p2_val < 17:  # Player 2 must draw if their value is below 17
        print(f"Player 2 hand: {player2} Value: {p2_val}")
        new_card = draw_for_player(player2)
        print("Player 2 drew:", new_card)
        player2_cards(player2)
        p2_val = value(player2)  # Recalculate value after drawing

    # Player 2 busts check
    if p2_val > 21:
        print(f"Player 2's hand value: {p2_val} - Player 2 busts!")
        return p2_val  # Return the busted value so we can check if Player 2 busted
    return p2_val


# Main game loop
def play():

    while True:
        playagain = input("would you like to play (again)?: ")
        if playagain in ["Yes", "yes", "Y", "y"]:
            t.clear()
            player1, player2 = deal_initial_cards()

            # Draw initial cards for both players
            display_player1_cards(player1)
            player2_cards(player2)

            # Player 1's turn
            p1_val = player1_turn(player1)

            #print(p1_val)

            # If Player 1 busted, skip Player 2's turn
            if p1_val > 21:
                print("Player 1 busts! Player 2 wins!")
                return

            # Player 2's turn (only if Player 1 didn't bust)
            p2_val = player2_turn(player2)

            # Determine the winner
            if p2_val > 21:
                print("Player 2 busts! Player 1 wins!")
            elif p1_val > p2_val:
                print("Player 1 wins!")
            elif p2_val > p1_val:
                print("Player 2 wins!")
            else:
                print("It's a tie!")
            playagain = input("would you like to play (again)?: ")
        elif playagain in ["No", "no", "N", "n"]:
            print("bye!")
            return False
        else:
            print("please use a valid input: yes or no ")
            continue


# Run the game
play()


