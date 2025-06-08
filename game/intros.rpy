label intro_0:

    # TODO: Add Mura's eyes for intro scene

    scene bg room
    show gabby temp at center

    g "Oh!"

    g "Hello? Is some one there? I can feel your presence."

    g "Oh, this is so exciting, I can't believe it actually worked"

    g "My names Gabby... Though right now I'm playing as Oracle"
    jump lets_talk

label intro_1:
    
    g "Hey there, Welcome back [persistent.player_name]."

    g "It's so good to see you return."

    g "You come back for another card reading?"

    jump lets_talk

label intro_2:

    g "Well hello again [persistent.player_name]."

    g "I'm glad to see you return one again."

    g "Hehe, was worried you might..."

    g "eh, never mind. You come for another reading?"

    jump lets_talk

label intro_3:
    
    g "Oh! Eheh, Welcome back [persistent.player_name]."

    g "It's so weird how you just pop back here like that..."

    g "Er, not that I mind or anything, I'm always happy to have a guest over."

    g "not very often I get...{w=0.5}{nw}"

    g "Uh! Oh, sorry. Never mind that. You probably want your reading, huh?"

    jump lets_talk

label intro_4:
    
    g "..."

    g "... Hrm?"

    g "Oh! You're back."

    g "Sorry,{w=0.5} I was just a little...{w=0.5} Distracted..."

    g "..."

    g "Oh right! You probably want your reading don't you? Heh, let's get to it shall we?"

    jump lets_talk

label intro_5:
    
    g "Hi again [persistent.player_name]"

    g "Sorry, but it is a bit of a busy day."

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