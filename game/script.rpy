# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[povname]")

define sky = Character("Skylar")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg mc bedroom

    "The letter from Skylar had been sitting on your bedroom table for months. You never really thought about having the need to move and start over until now, but it was time. You reach over and open the letter. Reading through it was more than enough to have your mind made up about it, you are moving to Seabloom Shores."

    "You pick up your phone to call Skylar and tell her you’re taking her up on the offer to move to Seabloom Shores."

    sky "Hello? I’m sorry I don’t recognize the number, who’s calling?"

    $ povname = renpy.input("What is your name?", length =32)

    sky "Oh!! Well, hello there, [povname]! Are you calling about moving to Seabloom Shores?"
    
    sky "Wonderful! Alright, well how about you get to town, and I’ll show you around and introduce you to some folks."

    "You take the bus to get to Seabloom Shores."

    "Skylar is there to greet you once you arrive."

    scene bg bus stop

    show skylar neutral at left

    sky "Hey, [povname]! Hope the bus ride wasn’t too bad but follow me! I’ll show you around."

    sky "Would you like to get something to eat or drink while we walk around? The cafe is just down the road!"

    hide skylar

    show bg cafe

    "You and Skylar head into the cafe."

    show skylar at left

    # This ends the game.

    return
