label intro_0:

    # TODO: Add Mura's eyes for intro scene

    scene bg room
    show gabby at center

    g "Oh!"

    g "Hello? Is some one there? I can sorta feel your presence."

    show gabby talk
    g "This is so exciting, I can't believe it actually worked!"

    g "Uhm, erherm..."

    show gabby dismissive
    g "Hello. I'm Gabby, Gabby Gibbson, Squee-hee! ^.^\n\nThough right now I'm playing as {color=#7d637c}Oracle{/color}... With her powers I am able to contact you the way I am now."

    hide gabby
    show oracle at center
    o "A pleasure to make your acquaintance, Viewer."

    hide oracle
    show gabby talk at center
    g "Oh right speaking of, what is your name stranger?"
    
    show gabby

    $ name_accepted = False
    $ name_redo = False
    while name_accepted == False:
        if name_redo == True:
            $ persistent.player_name = renpy.input("**Sigh** Ok then, let's try this again")
        else:
            $ persistent.player_name = renpy.input("Pst, you should let the mouse know what to call you.")
        
        if persistent.player_name == "":
            if name_redo == True:
                $ persistent.player_name = "Stranger"

                show gabby concerned

                m "Gabby, I believe our guest is wasting our time, perhapse we can find some one more interesting for you to play with."

                show gabby hurt
                g "Oh... Ok... Maybe next time then..."

                show gabby lookaway
                g "Still, Blessed Blee."

                $ renpy.quit()

            else:
                $ persistent.player_name = "Stranger"

                show gabby talk
                g "Oh, kind of the quiet type huh?...\nThat's alright, I'll just stick with Stranger then."

                g "Hehe, it sounds properly mysterious any way."
        
        else:
            if name_redo == True:
                show gabby shocked
                g "Hmph, thats going to take some getting used to, but I think I got it this time."

            else:
                show gabby shocked
                g "Huh, wow it's like I can barely even hear you... More like a feeling or a message.\n"    
        
        g "[persistent.player_name] was it? That sound right?"

        menu:
            "Yes":
                $ name_accepted = True
                show gabby talk
                g 'Oh good, I did "hear" it right then.'
            
            "No":
                $ name_redo = True
                show gabby concerned
                g "Oh shoot, My oracle powers must not be sharp enough yet.\nLet's try again."
    
    g "Well, welcome [persistent.player_name], let's begin!"

    jump lets_talk

label intro_1:
    
    show gabby at right
    with moveinright
    g "Hey there, Welcome back [persistent.player_name]."

    show gabby talk
    g "It's so good to see you return."
    
    show gabby sneaky
    g "You come back for another card reading?"

    jump lets_talk

label intro_2:

    show gabby at right
    with moveinright
    g "Well hello [persistent.player_name]."

    show gabby talk
    g "I'm glad to see you return one again."

    show gabby dismissive
    g "Hehe, was worried you might..."

    show gabby concerned
    g "eh, never mind. You come for another reading?"

    jump lets_talk

label intro_3:

    show gabby at right
    with moveinright   
    g "Oh! Eheh, Welcome back [persistent.player_name]."

    show gabby concerned
    g "It's so weird how you just pop back here like that..."

    show gabby lookaway
    g "Er, not that I mind or anything, I'm always happy to have a guest over."

    show gabby hurt
    g "not very often I get...{w=0.5}{nw}"

    show gabby concerned
    g "Eh! Oh, sorry... Never mind that. You probably want your reading, huh?"

    jump lets_talk

label intro_4:
    show gabby pensive at right
    with moveinright
    g "..."
    show gabby frown
    g "... Hrm?"

    g "Oh! You're back."
    show gabby hurt
    g "Sorry,{w=0.5} I was just a little...{w=0.5} Distracted..."

    g "..."
    show gabby frown
    g "Oh right! You probably want your reading don't you? Heh, let's get to it shall we?"

    jump lets_talk

label intro_5:
    show gabby at right
    with moveinright
    g "Hi again [persistent.player_name]"

    show gabby dismissive
    g "Sorry, but it is a bit of a busy day."

    show gabby talk
    g "I hope you don't mind if we are quick with your reading today."

    jump one_card

label intro_6:
    
    "intro 6"
    jump lets_talk

label intro_7:
    
    "intro 7"
    jump lets_talk

label intro_8:
    
    "intro 8"
    jump lets_talk

label intro_9:
    
    "intro 9"
    jump lets_talk

label intro_10:

    "intro 10"
    jump lets_talk

label intro_gone:

    scene bg loading
    pause
    jump intro_gone