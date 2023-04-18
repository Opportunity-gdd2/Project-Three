# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define s = Character("Sigrun")

define o = Character("Odin")

define po = Character("Pope")

define ev = Character("Evil Vampire")

define nv = Character("Vampire")

define m = Character("Mab")

define hm = Character("Hugin and Munin")

define a = Character("The Archive")

define fa = Character("Fairy")

define d = Character("Ferrovax")

define pl = Character("[player_name]")

# The game starts here.

label start:

    # Start Background Music As The Game Starts
    # Commented Out For Now. To Be Used Again Once Title and Game Music Are Different
    
    #play music "audio/BGM_Generic.mp3" fadein 2.0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    $ player_name = renpy.input("Okay, all that's left is for you to sign at the bottom")

    $ player_name = player_name.strip() or "Barnaby"

    pl "Hey it's me, [player_name]"

    # This ends the game.

    menu test:
        "Testing input"

        "Test A":
            "I pressed Test A"
        "Test B":
            "I pressed Test B"

    label after_menu:
    return
