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


# Variables declared here
# measure of how much evidence/suspicion the player has for the pope
default pope_score = 0
# default bomb evidence to false
default bomb_found = False
# do you have evidence to acquit the vampires?
default vamp_evidence = False
# who have you met?
default met_pope = False
default et_ev = False
default met_nv = False
default met_m = False
default met_hm = False
default met_a = False
default met_fa = False
default met_d = False


# The game starts here.

label start:

    # Start Background Music As The Game Starts
    # Commented Out For Now. To Be Used Again Once Title and Game Music Are Different
    
    #play music "audio/BGM_Generic.mp3" fadein 2.0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene monocsecurities

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show sigrun happy

    # These display lines of dialogue.

    $ player_name = renpy.input("Okay, all that's left is for you to sign at the bottom")

    $ player_name = player_name.strip() or "Barnaby"

    s "Perfect, you're officially a member of Monoc Securities, [player_name]."
    
    menu intro:
        "Choose your response."

        "Excited to get started!":
            pl "Excited to get started!"
        "Glad to be done with paperwork… finally.":
            pl "Glad to be done with paperwork… finally."

    s "Well, we’re glad to have you joining us.  Especially at such an exciting time."

    pl "Really? What’s going on?"

    s "Monoc Securities has just taken on a huge job, the kind of thing that requires strong, reliable security that only we can provide."

    menu sigrun1:
        "Choose your response."

        "Sounds like a big deal.":
            pl "Sounds like a big deal."
            s "It definitely is, but I think you should hear the details from the boss himself."
        "I’m sure I can handle it.":
            pl "I’m sure I can handle it.."
            hide sigrun happy
            show sigrun content
            s "Let’s not get too overconfident, you don’t even know the details of the job yet!"

    hide sigrun content
    show sigrun happy

    s "Speaking of which, I’m supposed to bring you to the boss so he can fill you in."

    pl "The boss, huh?  What’re they like?"

    s "He’s a pretty tough guy, but he’s fair… Although, he has been known to fire people on the spot.  Just try not to mess up your first impression and you’ll be fine."

    pl "Cool… no pressure."

    scene bestoffice

    s "Odin, sir.  I’ve brought our new hire, [player_name]."

    hide sigrun happy
    show odin neutral

    o "Hm.  Welcome [player_name], glad to have you joining us."

    menu odin1:
        "Choose your response."

        "Uh… Hello, sir.":
            pl "Uh... Hello, sir."
            hide odin neutral
            show odin lookaway
            o "C’mon, this is your introduction.  Give it a little more effort than that!"
            pl "Nice to meet you, sir!"
            hide odin lookaway
            show odin happy
            o "That’s better.  Now then, onto business."

        "Pleasure to meet you, sir.":
            pl "Pleasure to meet you, sir."
            hide odin neutral
            show odin happy
            o "Good introduction, but enough formalities, let’s get to business."

        "‘sup Cyclops!":
            pl "‘sup Cyclops!"
            hide odin neutral
            show odin annoyed
            o "Quite the rude recruit aren’t they.  Sigrun, get rid of this one and find someone with better people skills."
            hide odin annoyed
            show sigrun neutral
            s "I did tell you not to screw up your introduction."
            return
            # This ends the game.

    show odin happy

    o "I’m sure you’ve heard that Monoc Securities have recently agreed to a very large job."

    menu odin2:
        "Choose your response."

        "I have, I was hoping to learn a little bit more about that from you.":
            pl "I have, I was hoping to learn a little bit more about that from you."
            o "Good, then let me fill you in."
        "What are we talking about?":
            pl "What are we talking about?"
            hide odin happy
            show odin eyesclosed
            o "(sigh), alright, pay attention.  This is critical information."

    hide odin eyesclosed
    show odin neutral

    o "Each and every magical faction in the world is converging here in Chicago this week."

    o "The purpose is to draft and sign the Unseelie Accords, a vital treaty to ensure peace between those factions."

    o "All sorts of people will be there to sign this treaty, Fairies, Vampires, Dragons, The Archive, and of course, myself."

    pl "And we’re going to protect the venue?"

    o "Precisely.  You and other agents from Monoc Securities will be there to ensure the safety of all participants, including myself."

    o "We have no idea if anything is going to interrupt the signing, but I must make one thing clear: The accords are not unanimously popular."

    o "There are groups that have refused to sign, and we must not let them intervene."

    menu odin3:
        "Choose your response."

        "Sounds pretty serious, but I promise not to let you down.":
            pl "Sounds pretty serious, but I promise not to let you down."
            hide odin neutral
            show odin happy
            o "That’s what I like to hear, you have my full confidence."
        "Are you sure I’m up for a job this big?  I mean… I’ve only just started.":
            pl "Are you sure I’m up for a job this big?  I mean… I’ve only just started."
            hide odin neutral
            show odin happy
            o "This will be the perfect opportunity for you to sink or swim, and I’m sure you won’t let us down."
    
    hide odin happy
    show sigrun happy

    s "Same here, but in the meantime, why don’t you follow me and I’ll bring you to your office."

    scene office

    hide sigrun happy
    show sigrun happy

    s "Here we are, it’s a little under-decorated, but I’m sure you’ll make the most of it."

    menu office1:
        "Choose your response."

        "Looks… functional, at least.":
            pl "Looks… functional, at least."
        "It’ll work perfectly!":
            pl "It’ll work perfectly!"
    
    s "Yep! But while you’re getting situated, you should read through the basic training manual."

    s "Just remember to choose the best response in each scenario and it'll probably turn out fine."

    s "All right, ready to go?"

    pl "Go where?"

    s "The hotel venue where the Unseelie Accords are being signed.  We’d be pretty bad security if we showed up late."

    pl "Right, that makes sense."

    s "Once we get there we’ll need to be careful and vigilant.  Keep your eyes open for any suspicious behavior, and remember, those accords must be signed.  No matter what."

    label after_menu:





    # DAY TWO
    label day_two:
    scene day_two with fade
    scene hotelroom with fade

    if bomb_found:
        jump invest_bomb

    "The morning sun streams in through the flimsy hotel windows, waking me up long before I'd like to be."
    pl "Well...up and at'em I guess."
    "I take my time getting up and into uniform before heading out the door, and go to meet Odin and crew at his room."

    "*KNOCK KNOCK*"

    "???" "Fuck off!"

    pl "Sir? I'm here to escort you when you're ready."

    show odin annoyed

    o "I'm busy! Leave me alone!"

    hide odin annoyed

    "He slams the door in my face."

    pl "I guess I'll just wait here..."

    show sigrun neutral
    
    "After a few minutes, Sigrun joins me, but seems to already know not to knock."

    "We wait in silence."

    jump bomb_goes_off

    label invest_bomb:

    "I've barely slept at all and haven't been able to figure out at all what to expect."

    show sigrun worried at left
    show odin annoyed at right

    "I've already let the other's know that something is going on, but without much progress."

    s "And you're sure?"



    label bomb_goes_off:

    label bomb_not_off:



    label meet_everyone:


    label snoop_time:


    label vamp_evidence:

    label evening:



    label day_three:
    return
    # This ends the game.