
### Menu Skip ###

label main_menu:
    return

label start:

    scene black

    if not persistent.met_gabby:
        $ persistent.met_gabby = True
        jump intro_0
    
    elif persistent.gabby_gone == True:
        jump intro_gone

    else:
        scene bg room
        show gabby temp at right 
        with Dissolve(1.0)
        pause 0.5
        jump expression "intro_" + str(renpy.random.randint(1, 10))

label lets_talk:
    jump one_card

label one_card:
    
    $ card_draw_2 = fool
    $ tarot_deck.remove(card_draw_2)

    scene bg wood
    with PushMove(0.3, "pushup")

    pause 0.5

    show card_b at off_screen_top

    $ renpy.block_rollback()

    show card_b at deck_sit with ease

    o "Well then, shall we see what fate holds for you today?"

    o "let's see, your card is...{w=0.5}"


    $ invert = coin_flip()

    if invert == False:

        show card_flip_2

        pause 0.5

        o "... [card_draw_2.name]"

        o "this card represents [card_draw_2.upright]"

        if persistent.long_read == True:
            $ long_reader(o, card_draw_2.reading)

    else:

        show card_flip_2:
            rotate 180

        pause 0.5

        o "... [card_draw_2.name], inverted..."

        o "...when inverted this card represents [card_draw_2.reversed]."

        if persistent.long_read == True:
            $ long_reader(o, card_draw_2.inv_reading)

    o "Focus on this card, let it linger through your mind as you choose the paths to walk through your day"

    o "Allow it to subtely nudge your fate and guide you onto easier paths to walk."

    o "Though a warning, do not allow the mariad of negative possibilities cloud your vision. Allow it to simply be a beacon in the mists of uncertanty."

    o "No matter what the card may say you still have a will, and hey, some times a rougher path may be worth the journey."

    hide card_flip_2
    show single_return

    o "I hope your ventures through this cycle are fortunate. {w=0.5}"

    o "... and if not, well I hope a lesson is well learned for the future, for there is always something to be gained...{w=1.0} but only if you allow."

    o "But, for now I can feel the bindings of the platform weakening..."

    o "Merry meet.{w=0.5} Merry part.{w=0.5} And merry meet again."

    g "That means I hope to see you again, so please come and visit again ok...{w=3.0} Bye.{w=0.5}{nw}"

    $ renpy.quit()


label three_card:
    $ card_draw_1 = fool
    $ tarot_deck.remove(card_draw_1)
    $ card_draw_2 = renpy.random.choice(tarot_deck)
    $ tarot_deck.remove(card_draw_2)
    $ card_draw_3 = renpy.random.choice(tarot_deck)
    $ tarot_deck.remove(card_draw_3)

    scene bg wood
    with PushMove(0.3, "pushup")

    pause 0.5

    show card_b at off_screen_top

    $ renpy.block_rollback()

    show card_b at deck_sit with ease

    g "Here is a deck of cards."

    g "They may be flimsy, but they hold the power of fate."

    g "lets draw a card to represent a focus for your day"

    g "It is important to note these cards are not literal, but mearly meant to help guide your mind"

    ### Card 1 ###

    g "Let's see now..."

    pause 0.5
    $ renpy.block_rollback()
    $ invert = coin_flip()

    if invert == False:

        show card_flip_1

        g "... [card_draw_1.name]"

        g "this card represents [card_draw_1.upright]"

        if persistent.long_read == True:
            $ long_reader(card_draw_1.reading)

        hide card_flip_1
        show card_set_1

    else:

        show card_flip_1:
            rotate 180

        pause 0.5

        g "... [card_draw_1.name], inverted..."

        g "...when inverted this card represents [card_draw_1.reversed]."

        if persistent.long_read == True:
            $ long_reader(card_draw_1.inv_reading)

        hide card_flip_1
        show card_set_1:
            rotate 180

    g "Let's just put that over here.{w=1.0}"


    ### Card 2 ###

    g "now for your second card.{w=0.5}"


    $ invert = coin_flip()

    if invert == False:

        show card_flip_2

        g "... [card_draw_2.name]"

        g "this card represents [card_draw_2.upright]"

        if persistent.long_read == True:
            $ long_reader(card_draw_2.reading)

        hide card_flip_2
        show card_set_2

    else:

        show card_flip_2:
            rotate 180

        pause 0.5

        g "... [card_draw_2.name], inverted..."

        g "...when inverted this card represents [card_draw_2.reversed]."

        if persistent.long_read == True:
            $ long_reader(card_draw_2.inv_reading)

        hide card_flip_2
        show card_set_2:
            rotate 180

    g "Let's just set this in the center.{w=1.0}"

    #pause 1.0


    ### Card 3 ###


    g "Ok, last one..."

    pause 0.5

    $ invert = coin_flip()

    if invert == False:

        show card_flip_3

        g "... [card_draw_3.name]"

        g "this card represents [card_draw_3.upright]"

        if persistent.long_read == True:
            $ long_reader(card_draw_3.reading)

        hide card_flip_3
        show card_set_3

    else:

        show card_flip_3:
            rotate 180

        pause 0.5

        g "... [card_draw_3.name], inverted..."

        g "...when inverted this card represents [card_draw_3.reversed]."

        if persistent.long_read == True:
            $ long_reader(card_draw_3.inv_reading)

        hide card_flip_3
        show card_set_3:
            rotate 180

    g "We will of course just place that here to your right."

    $ tarot_deck.append(card_draw_1)
    $ tarot_deck.append(card_draw_2)
    $ tarot_deck.append(card_draw_3)

    pause 1.0

    g "And there you go."

    g "A simple card spread for your day."

    g "Hope it was a fortunate one. Reflect on their meaning as you pass the time. Maybe they will help you make some wise choices."

    g "Sorry the details are so vague (or missing), there is still much work to do, and fate is a tricky beast to tame."

    g "Hopefully it will be ready next time. ;3"

    g "Until then, Blessed Bleee! 🦒"

    $ renpy.quit()
