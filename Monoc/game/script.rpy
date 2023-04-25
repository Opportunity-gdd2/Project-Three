# The script of the game goes in this file.

$ import shake
# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen")

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
# is sigrun dead?
default sigrun_dead = False
# who have you met?
default met_pope = False
default met_ev = False
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

    scene monocsecurities with fade

    "I'm finally here"
    
    "Ahead of me, Monoc Securities rises, a bastion against the sun."
    
    "Today, I'll be joining the ranks of one of the most prestigious security agencies in the world, 
    protecting the natural and supernatural. It all starts here."

    "*THUNK*"

    "???" "Sorry about that! The doors aren't automatic."
    
    "Nice going, day one and you're already having to pick yourself off the ground."

    "???" "It's all good! I'm good."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show sigrun happy
    
    "???" "Well you must be our new hire, I'm Sigrun, I'll be your direct report, lets get started on your paperwork."

    scene niceoffice with fade
    show sigrun happy

    # These display lines of dialogue.
    show contract
    $ player_name = renpy.input("It goes surprisingly quickly, all that's left is to sign at the bottom")

    $ player_name = player_name.strip() or "Barnaby"
    hide contract
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
    scene day2 with MultipleTransition([
        False, Fade(0.5, 0.0, 0.5),
        "day2.png", Pause(1.0),
        True])
    #pause(delay = 1.0, hard = False)
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
    "..."
    "..."
    show odin annoyed

    "It's about an hour later when he emerges, and we walk down to the lobby"

    scene hotellobby
    show odin annoyed
    show sigrun neutral at left 
    o "Sigrun, go grab breakfast."

    s "Yes sir."

    hide sigrun with fade
    "In the meantime I look around the room, taking in who's here already."

    show dragon neutral at left
    show fairies neutral at left
    show archive neutral at right
    "The dragon and the fairies seem to be deep in conversation, while The Archive is just standing, staring at the wall"

    "All conversation pauses for a moment as a hotel employee runs out the door, gasping for air."

    o "That was weird-"

    jump bomb_goes_off

    label invest_bomb:

    "I've barely slept at all and haven't been able to figure out at all what to expect."

    show sigrun worried at left
    show odin annoyed at right

    "I've already let the other's know that something is going on, but without much progress."

    s "And you're sure?"

    pl "No- well, kind of? I did find this weird, white crystal stuff, and it doesn't act like salt. It disolves in water, but it's the wrong color when burned." 
    pl "I don't know if it's dangerous but still."

    s "Better safe than sorry."

    o "Oh please. You're all so worried over nothing. What could stop a god?"

    s "...I guess if you're not concerned... what do you think [pl]?"

    menu b_investigate_more:
        "I'd like to investigate around the hotel a little more":
            o "Fine, go see what you can find out"
            menu b_explorehotel:
                "Where should I look?"
                "Outside the hotel, around nearby alleys":
                    "Since I've seen the inside of the hotel, I'll check around the outside."

                    scene hoteloutside

                    "I try to look casual as I go around the area, searching for anything suspicious."

                    "Luckily, suspicious finds me, and I press against the wall to hide."

                    "??? A" "Have you done it?"

                    "??? B" "Yes, it's planted near the breakfast stand."
                    # Obscure this further or clarify based on playtests
                    "??? A" "Excellent, Ite missa est"
                    $ pope_score += 1
                    "Something's in the breakfast area? Better check it out."
                    jump breakfast_invest
                #"The other hotel rooms, eavesdropping on the other guests":
                
                "In the hotel lobby, asking the employees what they've seen":
                    "I think I'll ask a few of the employees about anything suspicious."

                    scene hotellobby

                    pl "Excuse me! I wanted to ask you a few questions."

                    "Concierge" "Of course! We have lots of lovely tours and restaurants available nearby, what are you interested in?"

                    pl "Oh uh, nothing like that, I was more wondering if you knew anything about this crystal stuff?"

                    "The concierge looks confused, and a little annoyed with my divergence from the script. He looks over at it anyway."

                    "Concierge" "I'm afraid it doesn't look familiar, did you find this here? How did you get this?"

                    pl "Oh I found it in the lobby yesterday, I was a bit concerned and so wanted to ask about it."

                    "This it seems, actually does interest him."

                    "Concierge" "Well, we'll call for one of our custodians and make sure to clean up, will that be all?"

                    pl "Yes, though it's a bit of an odd one. Have you seen anything suspicious? Anything odd?"

                    "Concierge" "Pardon?"

                    pl "Oh of course-"
                    
                    "I flash my new employee ID, Monoc Securities front and center."
                    
                    pl "It's for a job, I just wanted to check with you."

                    "Concierge" "Oh! Of course. Though I can't say there was anything suspicious that I saw, you're free to look around."

                    "A bit disappointed with no leads, I take my time looking around the lobby, though nothing turns up."
                    
                    "The last place to look is the breakfast nook, so once I've cleared that I'll report back to Odin."
                    jump breakfast_invest

                "Eavesdrop on Odin, Sigrun and Hugin and Munin":
                    scene hotellobby
                    "I make a few loud steps away from the door, to make it seem like I've left. Then I quietly step back toward the door and listen in."

                    o "Are you sure about them Sigrun?"

                    s "Well, they interviewed well, but seeing the way they've been acting I'm not so sure."

                    o "Yeah, personally, I'm not a fan of employees who can't take orders."

                    s "Pardon? What do you mean-"

                    scene hotelroom
                    show odin annoyed 
                    show sigrun annoyed at left
                    show besties annoyed at right
                    "SLAM"

                    o "Employees who would rather spy on their own company than do as they're told aren't needed here."

                    return
        "I'd like to send these crystals off for testing":
            $ sigrun_dead = True
            o "Ugh."

            s "Good plan. We'll get breakfast with Hugin and Munin and wait to hear back"

            "I nod and take off back to Monoc Securities."
            
            scene monocsecurities with fade
            
            "Chem lab...chem lab...chem lab!"
            
            pl "Hi! I need you guys to figure out what this is!"
            
            "Chem Lab Girl" "Uhhh, sure. Give me a bit."

            "It's only a few minutes later that I get a call from one of the twins"

            hm "You need to come back here. Now."

            pl "Why? What happened?"

            hm "A bomb went off, we're sending you the new address."

            with Shake((0,0,0,0),0.5,dist=10)
            
            pl "{fast}WHAT?!"

            hm "Odin, it's like the first time you've dealt with one of these or something."

            pl "It is!"

            hm "Oh. Well, Sigrun's dead so we need you to come back here."

            pl "Of course-Wait what about the crystals?"

            hm "Have them call you with what it is?? How did you get hired? Your boss was almost bombed and you can't do anything without direction."

            "Hopefully I still have a job when I get back."

            scene hotellobby with fade
            show odin annoyed
            show besties annoyed at left

            o "About time you got back!"

            pl "Sorry!"

            "Just then my phone rings"

            pl "Hello?"

            "???" "Hi is this [pl]?"

            pl "Yes who is this?"

            "Chem Lab Girl" "I'm the one you handed the crystals off to, we've run a few tests and it looks like ammonium nitrate."

            pl "And what is that for?"

            "Chem Lab Girl" "Mostly gardening."

            pl "Are you sure? Is that all it's used for?"

            "Chem Lab Girl" "Sometimes bombs too but it's not very likely, there's better options."

            pl "Well. A bomb just went off."

            "Chem Lab Girl" "Oh! So then yeah probably for the bomb."

            "Very helpful."

            pl "Well, the crystals might have been used for the bomb."

            o "You think?! Whatever, just go do your job, I'm going to checkout the new room."

            pl "Yes sir..."
            jump meeting_post_bomb

        "I trust Odin's judgement":

            hide odin annoyed at right
            show odin happy
            o "A wise choice kid. Let's go get some breakfast now that everyone's calmed down."
            scene hotellobby with fade
            show odin happy
            show sigrun neutral at left 
            o "Sigrun, go grab breakfast."

            s "Yes sir."

            hide sigrun with fade
            "In the meantime I look around the room, taking in who's here already."

            show dragon at left
            show fairies at left
            show archive neutral at right
            "The dragon and the fairies seem to be deep in conversation, while The Archive is just standing, staring at the wall"

            "All conversation pauses for a moment as a hotel employee runs out the door, gasping for air."

            o "That was weird-"

            jump bomb_goes_off

    label bomb_goes_off:

    $ sigrun_dead = True
    show odin eyesclosed
    "BOOM"
    with Shake((0,0,0,0),1.0,dist=40)
    show odin annoyed
    "{fast}There's screaming, and everyone is running. Some reflex takes over, and before I know it, I'm outside and Odin is behind me, safe."

    scene hoteloutside
    show odin neutral
    pl "Are you okay?"

    o "Yes, I'm fine. You did good kid."

    pl "Where are the others?"

    show besties neutral at left
    hm "We're here."

    "But as I look around I don't see Sigrun, just the hotel, entrance now crumbling."

    "Someone else has called an ambulance, and a firetruck comes to a hard stop."
    "..."
    "..."
    "We wait, for what seems like hours, but when we move to a different hotel, Sigrun isn't with us."

    scene hotellobby
    show odin neutral
    show besties neutral at left
    pl "What would you like to do now?"

    o "You go do what you need to, I'll stay in my room with Hugin and Munin."

    "I almost protest, but think better of it."
    hide odin neutral
    hide hm
    jump meeting_post_bomb

    label breakfast_invest:

    "As the rest of the hotel begins to wake up, it's starting to become difficult to not look like I'm crazy poking around here."
    
    "Nothing in the muffins, the coffee is burnt but not suspicious, and I'm about to give up when I see it just under the tablecloth..."

    "A little trace of white crystals, almost mistakable for tablesalt, just like the sample I'm carrying with me."

    menu check_table:
        "Look under the tablecloth":
            "I gently lift the cloth, and there, nestled against the wall and covered to look like the wall paper, is a small package."
            "I peel it off the wall and look at it. Almost Loony Tunes esque, in my hand is what looks like a replica version of a missle, and it's packed with the white powder."
            menu disarm_bomb:
                "It's cute, I should go show it to Sigrun":
                    show sigrun content
                    s "Hey! Find anything?"
                    show sigrun worried
                    "BOOM"
                    with Shake((0,0,0,0),1.0,dist=40)
                    "I'm not even around long enough to understand what happened, but Sigrun's worried face tells me enough."
                    "Probably shouldn't have treated that so lightly"
                    with Fade(5.0)
                    return
                "Just to be safe, I'm going to dunk it in water":
                    "I don't know if it's actually dangerous but I mean, worst case I've waterlogged someone's suspicious toy"
                    
                    show sigrun content
                    
                    s "Hey! Find anything?"
                    
                    pl "Just this weird toy, bomb, thing."

                    s "Oh shit"

                    pl "What?"

                    s "Well ah, while you were looking around I tested more of the crystals. It's ammonium nitrate, you can use it to make bonbs."

                    pl "It's pretty cute for a real bomb don't you think?"

                    s "Well. I guess once the nitrate has disolved we can see what else was in there and confirm."

                    "So we wait, and when the bomb/toy seems almost empty we pull it out."

                    s "Yeah, those are charges, good job Bomb Squad."

                    "Bomb Squad" "You think that'll stick?"
                    
                    s "No, you'll be back to [pl] in a bit, we don't really do nicknames."

                    pl ":("

                    s "Anyway stop messing around we've gotta tell everyone."
                    jump meeting_no_bomb
        "Ignore it and go about your business":
            "Well, it's probably nothing right?"
            show sigrun content
            s "Hey! Find anything?"
            show sigrun worried
            "BOOM"
            with Shake((0,0,0,0),1.0,dist=40)
            "I'm not even around long enough to understand what happened, but Sigrun's worried face tells me enough."
            "Probably shouldn't have ignored that..."
            with Fade(5.0)
            return

    # placeholder, mvp
    label meeting_post_bomb:
    "I decide to meet the people I haven't so far, and maybe see what they know."
    menu meet_everyone:
        "Who should I see first?"
        "I think I've met everyone I care to know.":
            jump snoop_time
        "I'll introduce myself to The Pope" if not met_pope:
            show pope neutral
            pl "Hello Pope, I'm [pl]"
            po "Hi [pl] I'm a little shaken up, but not as shaken up as you might expect me to be"
            $ met_pope = True
            $ pope_score += 1
            hide pope neutral
            jump meet_everyone
        "I'll introduce myself to one of the vampires" if not met_ev:
            show vampirebad neutral
            pl "Hi! I'm [pl], who are you?"
            ev "Bleh bleh bleh! I'm a vampire! But not a very nice one!"
            $ met_ev = True
            hide vampirebad neutral
            jump meet_everyone
        "I'll introduce myself to one of the other vampires" if not met_nv:
            show vampirechill neutral
            pl "Hi! I'm [pl], who are you?"
            nv "Hi [pl], I'm a very chill vampire."
            $ met_nv = True
            hide vampirechill neutral
            jump meet_everyone
        "I'll introduce myself to Queen Mab" if not met_m:
            show mab neutral
            pl "Hello your majesty! I'm [pl]."
            m "I'm the organizer, and so am upset that the meeting has gone wrong, but I will do anything to get the accords signed."
            $ met_m = True
            hide mab neutral
            jump meet_everyone
        "I'll introduce myself to the dragon" if not met_d:
            show dragon neutral
            pl "Hi! I'm [pl], who are you?"
            d "I'm Ferrovax, I am older than mankind and just here for the food :)"
            $ met_d = True
            hide dragon neutral
            jump meet_everyone
        "I'll introduce myself to the fairies" if not met_fa:
            show fairy neutral
            pl "Hi! I'm [pl], who are you?"
            fa "We're Puck, Titania and Oberron, and we're just kind of following Mab's lead."
            $ met_fa = True
            hide fairy neutral
            jump meet_everyone
        "I'll introduce myself to The Archive" if not met_a:
            show archive neutral
            pl "Hello Archive, I'm [pl], nice to meet you."
            a "Ah, so you were the one just hired on by Monoc."
            pl "0.0 Wow"
            $ met_a = True
            hide archive neutral
            jump meet_everyone



    label meeting_no_bomb:
    "We tell Odin what I found, and then gather everyone in the lobby to let them know what I found."
    # show whatever people we want
    pl "Okay so there was a bomb in the breakfast area."

    "This sets off a chorus of whispers, and more than a few dirty looks."

    s "Have some tact!"

    "Sigrun re-explains what happened, much more professionally than I did. When she finishes she turns to me."

    pl "So what now."

    s "Now you investigate, see if anyone's acting weird."

    menu meet_everyone_no_bomb:
        "Who should I see first?"
        "I think I've met everyone I care to know.":
            jump snoop_time
        "I'll introduce myself to The Pope" if not met_pope:
            show pope neutral
            pl "Hello Pope, I'm [pl]"
            po "Hi [pl] I'm a little shaken up, but not as shaken up as you might expect me to be"
            $ met_pope = True
            $ pope_score += 1
            hide pope neutral
            jump meet_everyone_no_bomb
        "I'll introduce myself to one of the vampires" if not met_ev:
            show vampirebad neutral
            pl "Hi! I'm [pl], who are you?"
            ev "Bleh bleh bleh! I'm a vampire! But not a very nice one!"
            $ met_ev = True
            hide vampirebad neutral
            jump meet_everyone_no_bomb
        "I'll introduce myself to one of the other vampires" if not met_nv:
            show vampirechill neutral
            pl "Hi! I'm [pl], who are you?"
            nv "Hi [pl], I'm a very chill vampire."
            $ met_nv = True
            hide vampirechill neutral
            jump meet_everyone_no_bomb
        "I'll introduce myself to Queen Mab" if not met_m:
            show mab neutral
            pl "Hello your majesty! I'm [pl]."
            m "I'm the organizer, and so am upset that the meeting has gone wrong, but I will do anything to get the accords signed."
            $ met_m = True
            hide mab neutral
            jump meet_everyone_no_bomb
        "I'll introduce myself to the dragon" if not met_d:
            show dragon neutral
            pl "Hi! I'm [pl], who are you?"
            d "I'm Ferrovax, I am older than mankind and just here for the food :)"
            $ met_d = True
            hide dragon neutral
            jump meet_everyone_no_bomb
        "I'll introduce myself to the fairies" if not met_fa:
            show fairy neutral
            pl "Hi! I'm [pl], who are you?"
            fa "We're Puck, Titania and Oberron, and we're just kind of following Mab's lead."
            $ met_fa = True
            hide fairy neutral
            jump meet_everyone_no_bomb
        "I'll introduce myself to The Archive" if not met_a:
            show archive neutral
            pl "Hello Archive, I'm [pl], nice to meet you."
            a "Ah, so you were the one just hired on by Monoc."
            pl "0.0 Wow"
            $ met_a = True
            hide archive neutral
            jump meet_everyone_no_bomb

    label snoop_time:
    "There wasn't a lot to learn from anyone, or at least nothing people were willing to admit to. So I decide to head back to the previous hotel and look around."
    "I call Odin's room, and let him know where I'm heading so he doesn't leave."
    #label vamp_evidence:

    #label evening:



    label day_three:
    return
    # This ends the game.
