### Image Values ###

image card_b = resize("cards/b.webp")

image card_1 = resize("cards/[card_draw_1.index].webp")
image card_2 = resize("cards/[card_draw_2.index].webp")
image card_3 = resize("cards/[card_draw_3.index].webp")


### Transforms ###

transform off_screen_top:
    xpos 0.5
    ypos -0.5


transform deck_sit:
    xpos 0.5
    ypos 0.25


transform resize:
    zoom 0.25
    anchor (0.5, 0.5)



######################
##### Animations #####
######################


### Card 1 animation ###

image card_flip_1:
    "card_b"
    deck_sit
    parallel:
        linear 0.25 ypos 0.5
    parallel:
        ease 0.2 xzoom 0.01
    parallel:
        ease 0.2 yzoom 1.1

    "card_1"
    xzoom 0.01 yzoom 1.1
    parallel:
        ease 0.2 xzoom 1.2
    parallel:
        ease 0.2 yzoom 1.2

image card_set_1:
    "card_1"
    xpos 0.5 ypos 0.5
    xzoom 1.2 yzoom 1.2
    parallel:
        ease 0.5 xpos 0.25 ypos 0.75
    parallel:
        linear 0.5 xzoom 1.0 yzoom 1.0 


### Card 2 animation ###

image card_flip_2:
    "card_b"
    deck_sit
    parallel:
        linear 0.25 ypos 0.5
    parallel:
        ease 0.2 xzoom 0.01
    parallel:
        ease 0.2 yzoom 1.1

    "card_2"
    xzoom 0.01 yzoom 1.1
    parallel:
        ease 0.2 xzoom 1.2
    parallel:
        ease 0.2 yzoom 1.2

image card_set_2:
    "card_2"
    xpos 0.5 ypos 0.5
    xzoom 1.2 yzoom 1.2
    parallel:
        ease 0.5 ypos 0.75
    parallel:
        linear 0.5 xzoom 1.0 yzoom 1.0 


### Card 3 animation ###

image card_flip_3:
    "card_b"
    deck_sit
    parallel:
        linear 0.25 ypos 0.5
    parallel:
        ease 0.2 xzoom 0.01
    parallel:
        ease 0.2 yzoom 1.1

    "card_3"
    xzoom 0.01 yzoom 1.1
    parallel:
        ease 0.2 xzoom 1.2
    parallel:
        ease 0.2 yzoom 1.2

image card_set_3:
    "card_3"
    xpos 0.5 ypos 0.5
    xzoom 1.2 yzoom 1.2
    parallel:
        ease 0.5 xpos 0.75 ypos 0.75
    parallel:
        linear 0.5 xzoom 1.0 yzoom 1.0 

### return cards to deck ###

image single_return:
    "card_2"
    xpos 0.5 ypos 0.5
    xzoom 1.2 yzoom 1.2
    parallel:
        easein 0.2 xzoom 0.01
    parallel:
        easein 0.2 yzoom 1.1

    "card_b"
    xzoom 0.01 yzoom 1.1
    parallel:
        easeout 0.2 xzoom 1.0
    parallel:
        easeout 0.2 yzoom 1.0
    parallel:
        linear 0.3 deck_sit



################################
###### Animation Function ######
################################
