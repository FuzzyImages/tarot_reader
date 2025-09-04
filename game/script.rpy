
### Menu Skip ###

label main_menu:
    return

label start:

    scene black
    play music bg_music volume 0.7 fadein 1.0
    if not persistent.met_gabby:
        jump intro_0
    
    elif persistent.gabby_gone == True:
        jump intro_gone

    else:
        scene bg room
        with Dissolve(1.0)
        pause 0.5
        jump expression "intro_" + str(renpy.random.randint(1, 5))

label lets_talk:
    
    show gabby concerned
    if persistent.met_gabby == False:
        g "Sorry but I havn't yet prepared for full tarot readings"

        g "Currently I'm only able to do a single card reading.\nThese are better known as a one-card pull, or a daily draw."

        g "You are going to want to focus on this single card and reflect on it for your day."

        g 'Oh and I also only have the major arcana done and can only give you their upright meanings at this time. -.-'

        show gabby talk
        g "I hope that is ok friend. ^.^;"

        $ persistent.met_gabby = True

    else:
        show gabby concerned
        g "Sorry to say, I still have not completed the rest of the cards and their meanings.\nThese things take a lot more time than I expect some times. -.-;"
        show gabby
        g "But we can still do a daily draw if that's ok. Just like usual, focus on the card as Oracle makes her reading."

    jump one_card

label one_card:
    
    $ card_draw_2 = renpy.random.choice(tarot_deck)
    $ tarot_deck.remove(card_draw_2)

    scene bg wood
    with PushMove(0.3, "pushup")

    pause 0.5

    show card_b at off_screen_top
    play sound card_slide_sfx

    $ renpy.block_rollback()

    show card_b at deck_sit with ease

    o "Well now traveler, shall we see what fate holds for you today?"

    o "let's see. Your card today is...{w=0.5}"


    $ invert = False

    if invert == False:

        show card_flip_2
        play sound card_flip_sfx

        pause 0.5

        o "... [card_draw_2.name]"

        o "This card represents [card_draw_2.keywords_upright]."

        if persistent.card_descriptions == True:
            $ card_draw_2.read_description()

        if persistent.card_readings == True:
            $ card_draw_2.do_reading()

    else:

        show card_flip_2:
            rotate 180

        pause 0.5

        o "... [card_draw_2.name], inverted..."

        o "...when inverted this card represents [card_draw_2.reversed]."

        if persistent.long_read == True:
            $ long_reader(o, card_draw_2.inv_reading)

    o "Focus on this card, let it linger through your mind as you choose the paths to walk through your day."

    o "Allow it to subtely nudge your fate and guide you onto easier paths to walk."

    o "Though a warning, do not allow the myriad of possibilities cloud your vision. Allow it to simply be a beacon in the mists of uncertanty."

    o "No matter what the cards may say, you still have a will of your own... Besides, some times a rougher road may be worth the journey."

    hide card_flip_2
    show single_return
    play sound card_flip_sfx

    o "I hope your ventures through this cycle are fortunate. {w=0.5}"

    o "... and if not, well I hope a lesson is well learned for the future, for there is always something to be gained...{w=1.0} but only if you allow."

    o "But, for now I can feel the threads connecting us begining to weaken..."

    o "Merry we meet,{w=0.5} merry we part,{w=0.5} and merry we meet again."

    g "That's Oracles way of saying \"hope to see you again\", so please come and visit again ok...{w=3.0}Well...{w=1.0} bye.{w=0.5}{nw}"

    scene black
    $ renpy.quit()


label three_card:
    $ card_draw_1 = tarot_deck[0]
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
