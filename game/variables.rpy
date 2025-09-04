### Persistent Variables ###
default debug = False

default persistent.player_name = "Stranger"
default persistent.gabby_hurt = False
default persistent.gabby_gone = False
default persistent.gabby_moody = False
default persistent.met_gabby = False
default persistent.card_descriptions = True
default persistent.card_readings = True
default persistent.lore_text = True
default persistent.one_reading = False
default persistent.giraffe = True

### Defaults Values ### 

default card_draw_1 = "0"
default card_draw_2 = "0"
default card_draw_3 = "0"
default inverted = False

### Character Defines ###

define g = Character("Gabby", who_color="7d637c")
define o = Character("Oracle", who_color="7d637c")
define m = Character("???", who_color="134e3c")

### Define Audio tracks ###

define audio.bg_music = "audio/fantasy-medieval-mystery-ambient.mp3"
define audio.card_slide_sfx = "audio/card_slide.ogg"
define audio.card_flip_sfx = "audio/card_flip.ogg"