# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define sky = Character("Skylar")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    "The letter from Skylar had been sitting on your bedroom table for months. You never really thought about having the need to move and start over until now, but it was time. You reach over and open the letter. Reading through it was more than enough to have your mind made up about it, you are moving to Seabloom Shores."

    "You pick up your phone to call Skylar and tell her you’re taking her up on the offer to move to Seabloom Shores."

    show skylar neutral at left

    sky "Hello? I’m sorry I don’t recognize the number, who’s calling?"

    # This ends the game.

    return
