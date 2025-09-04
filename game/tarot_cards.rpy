init python:
    import itertools

    tarot_deck = []

    class TarotCardBuilder:
        def __init__(self):
            self.card = TarotCard()

        def index(self, index):
            self.card.index = index
            return self

        def value(self, value):
            self.card.value = value
            return self

        def major_arcana(self, is_major):
            self.card.major_arcana = is_major
            return self

        def name(self, name):
            self.card.name = name
            return self

        def keywords_upright(self, keywords_upright):
            self.card.keywords_upright = keywords_upright
            return self

        def keywords_reversed(self, keywords_reversed):
            self.card.keywords_reversed = keywords_reversed
            return self

        def description(self, description):
            self.card.description = description
            return self

        def reading(self, reading):
            self.card.reading = reading
            return self

        def inv_reading(self, inv_reading):
            self.card.inv_reading = inv_reading
            return self

        def build(self):
            tarot_deck.append(self.card)
            return self.card

    class TarotCard:
        def __init__(self):
            self.index = None
            self.value = None
            self.inverted = False
            self.major_arcana = None
            self.name = None
            self.keywords_upright = "Hrm, I don't recall..."
            self.keywords_reversed = "Hrm, I don't recall..."
            self.description = ["On this card we see....", "Oops, this card's art must not be done yet. Sorry about that... ^^;"]
            self.reading = ["It means...", "Errr...", "Uhhhm...", "I forgot...", "...", "Oh well!"]
            self.inv_reading = ["It means...", "Errr...", "Uhhhm...", "I forgot...", "...", "Oh well!"]

        def read_description(self):
            for line in self.description:
                renpy.say(o, line)

        def do_reading(self):
            if self.inverted:
                lines = self.inv_reading
            else:
                lines = self.reading

            for line in lines:
                renpy.say(o, line)


        def position(self):
            self.inverted = renpy.random.choice([True, False])
            
# Define all cards
define fool = (TarotCardBuilder()
    .index(0).value(0).major_arcana(True).name("The Fool")
    .keywords_upright("beginning, innocence, spontaneity, and a free spirit")
    .keywords_reversed("holding back, recklessness, and risk-taking")
    .description([
        "The Fool is number 0 in the major arcana, and though as a number it may seem to represent nothingness, that does not mean it is without value.",
        "Just as the circle has no beginning or end, so too is the Fool an expression of limitless potential and growth.\nLike an empty container awaiting to be filled.",
        "On it we can see a young mouse ready to make their trec into an exciting new world, with little more than their clothing and the supplies upon their shoulder.",
        "Though they wander with joy and enthusiasm, they walk naively towards the perils of the cliffs ahead.",
        "Along for their journey is a small companion, at their side not only to give warning of what lies ahead, but also to remind that one does not have to walk these winding roads alone."
    ])
    .reading([
        "The Fool is the card of wanderers and adventure.",
        "Just as The Fool, you are on the precipice of uncertainty and gazing into the unknown potential of what lies ahead.",
        "Now is a good time for something new, to take that risky step into the uncertain.",
        "Perhaps your anxieties are restraining your thoughts and willingness to move forward, but just like The Fool, you should set aside the fears and think of not only what you have to potentially lose, but more importantly what you may fail to gain.",
        "Though be sure to look before you leap. Just because you should have the courage to embrace the new, you should also be aware of the very real risk that may lie within.",
        "After all, there is a big difference between naivety and simple pure foolishness."
    ])
    .inv_reading([
        "Just as the Fool represents potential and the possible, it can equally be a warning of your own ability to limit that potential.",
        "Inverted The Fool acts as a messenger of your self imposed limitations.",
        "Perhaps your anxieties or fears have left you unwilling to act, or maybe you are overwhelmed by the limitless possibilities that can go wrong.",
        "Either way, you have something you desire and you have restrained yourself from achieving it, or possibly from even taking the first step.",
        "It is ok to slow down and take stock of these ideas and desires, you need to allow yourself to unpack and analyze the why and how to achieve your goals.",
        "I suggest perhaps you make a list of the pro’s and con’s.",
        "It is important to remember that this representation is only the opposite side to the same beginning as The Fool’s upright meaning, as some adventures are not so spontaneous, and you need to know where to go to eventually arrive there.",
        "But, in the end, you are the only one who can shackle yourself into stagnation, and it is upon you to free yourself of that weight."
    ])
    .build())

define magician = (TarotCardBuilder()
    .index(1).value(1).major_arcana(True).name("The Magician")
    .keywords_upright("manifestation, willpower, resourcfulness, skill, and creativity")
    .description([
        "Just as the number 1 represents the start of most things, so too does the Magician symbolize new beginnings and opportunity.",
        "The Magician is the card of creatives and the mark of the inspired.",
        "They point one hand to the sky and the other to the ground, showing a balance between The Giraffe’s higher planes above and the stability of the Earth below.",
        "In their paw they wield a wand shaped like a two-ended candle, a symbol of manifestation granted by the flames of the Phoenix.",
        "Above their head rests an infinity symbol, representing limitless creativity gifted by the generations that came before.",
        "Beside them on a table lie the four suits of the minor arcana: a stick, a cup, a sword, and a coin.",
        "These items represent the four elements, and together they are all the tools needed to manifest ideas into creation.",
        "Surrounding the Magician is an array of blooming flowers, a sign of blossoming ideas and inspiration."
    ])
    .reading([
        "As a master creative, the Magician brings forth all the tools you need to manifest your will into being — not with a hammer or a brush, but with inspiration and your own will.",
        "At this moment you may hold the seed of an idea, and you need only give it the resources to grow.",
        "Do not be swayed by tempting thoughts of coins or the cheers of others.",
        "This is a time to nurture your desires with deeper motivations of emotional and personal fulfillment.",
        "Be willing to explore and gather the resources you may need.",
        "But remember — what you create is a part of you, and it should reflect your intentionality.",
        "Be methodical and aware of what lies within that reflection, for you do not want to see someone else staring back from the mirror of your soul."
    ])
    .build())

define high_priestess = (TarotCardBuilder()
    .index(2).value(2).major_arcana(True).name("The High Priestess")
    .keywords_upright("intuition, spirituality, inner voice, and the subconciouse mind")
    .description([
        "The Oracle acts as the guardian to the unknown and sacred knowledge of the spiritual realm.",
        "She sits before a tapestry adorned with pomegranates, a symbol of abundance and fertility, behind which the spiritual realms lie.",
        "The tapestry hangs between two pillars, one black and one white, representing the nature of duality.",
        "All things have opposites, whether it be good and evil, man and woman, or Earth and the Ethereal.",
        "Though these may be opposites, they are not in opposition, and serve together to hold the veil.",
        "The Oracle is adorned in robes and wears the symbol of The Giraffe to reflect her attachment with its foresight and wisdom.",
        "In her paws a rolled up parchment partially concealed by her robes, showing her grasp on old partially lost knowledge.",
        "And her foot rests on a crescent, revealing her to be grounded in her femininity, the cycles of nature and time, as well as her understanding of the unknown represented by the moon.",
    ])
    .reading([
        "The Oracle acts as a guide between the conscious and subconscious mind.",
        "There are many things you may not be aware of within yourself, and worse yet you may actively subdue and hide.",
        "This card seeks to aid you in connecting with your inner self and accept that which is within you.",
        "Now is a good time to look inward and bring some of what is inside out of you.",
        "In many ways the Oracle represents one's femininity (regardless of your sex or gender) it is an aspect of oneself many repress in some manner or another.",
        "Allow your inner voice to speak and reflect on how you present yourself to others.",
        "This also means you should equally trust in your intuition, to not second guess yourself in your current affairs and situation.",
        "Sometimes you may be surprised to find your own overthinking will only serve to complicate your understanding of things.",
    ])
    .build())

define empress = (TarotCardBuilder()
    .index(3).value(3).major_arcana(True).name("The Empress")
    .keywords_upright("femininity, fertility, creativity, nurturing, beauty, and nature")
    .description([
        "The Empress is embodied by the image of a beautiful well figured mouse resting at peace within the tranquility of nature, showing her connection with the land.",
        "Around her an abundance of pomegranates, a symbol of fertility, as well as a field of wheat before her, a sign of prosperity.",
        "She rests atop a bed of luxurious cushions and velvet, one dawning the symbol of venus, another sign of her ties to femininity, fertility, beauty, and the act of creation.",
        "In her hair 12 stars rest to show connection with the celestial cycles and the tapestries of the higher planes above.",
    ])
    .reading([
        "I believe it would be easy to guess that this card represents one's connection to their femininity.",
        "Regardless of your gender, it is important to embrace the side of you that pertains to a nurturing spirit.",
        "This does not strictly mean a sense of motherhood, but the willingness to show connection with those close and important to you.",
        "Similarly, The Empress is a symbol of fertility and birth.",
        "You may see this as literal or metaphorical as you wish to interpret it, to be a mother does not mean one has to birth a child, and equally too, one may birth an idea to be manifested into reality with as much care.",
        "The Empress also reveals herself to remind one to reflect on their good fortunes.",
        "Take account of the blessings you may have, even if they are few, it is important to value what fortune you have in life.",
        "Just as The Empress is connected to the Earth around her, so should you be connected with the environment you find yourself in, this will give you some peace of mind or perhaps an understanding of what needs to be done.",
        "Whatever this card may represent in your mind, it is simply important to approach it with passion and sensitivity.",
    ])
    .build())

define emperor = (TarotCardBuilder()
    .index(4).value(4).major_arcana(True).name("The Emporer")
    .keywords_upright("masculinity, structure, authority, protection, and discipline")
    .description([
        "As The Empress is the mother figure, so too is The Emperor a symbol of the father. He is dressed with a red robe, presenting his power and vitality.",
        "But, Underneath he dawns a suit of armor to protect him from both physical and emotional vulnerability.",
        "He shows age with a thick beard, signifying his wisdom and experience.",
        "Along with a crown and golden sphere in his paw to show the authority he commands.",
        "In his other paw he wields a rod in the image of The Giraffe, a symbol for the guidance he has gained from those above him.",
        "The Emperor sits upon a stone throne with a mountain range at his back, a sign of the firm unshakable foundation.",
        "On the throne are ram heads that represent Aries, along with Mars in the sky to show his attachment to the masculine, all conveying an adherence to tradition and a resistance to change.",
        "Though viewed closely one can see at the mountain's base flows a river, a sign for change to be possible with time.",
    ])
    .reading([
        "Just as The Emperor is the father of this deck, so too are you adopting a fatherly role within your life.",
        "While you may not be a father in the literal sense, now is the time for you to show some authority within the boundaries of your social circles.",
        "Yet again, regardless of your gender, you are being guided to embrace some of your masculine energies.",
        "Be assertive, protect those close to you, and give those that rely on you the solid footing they are in need of to succeed.",
        "You have gained experience with each passing year, no matter how short or long that may be at this stage of your life, this is a valuable resource to pass down to those around you.",
        "Share the experience you have and the wisdom you gathered, and act as a guide to those who may appear lost.",
        "The Emperor is also the symbol of tradition and rule, and regardless of your position on authority, you may be in need of structure in your life and others near you.",
        "Whether this is the need of strict rules and guidelines, or healthy boundaries, it is important that you remain firm and systematic in your plans to move forward.",
    ])
    .build())

define teacher = (TarotCardBuilder()
    .index(5).value(5).major_arcana(True).name("The Teacher")
    .keywords_upright("tradition, conformity, education, knowledge, and social structure")
    .description([
        "The Teacher acts as the masculine opposite of The Oracle.",
        "He sits within a temple, wearing three robes and a three tiered crown atop his head, both signifying his attachment to conscious, subconscious, and the superconscious that form our perceptions of the world.",
        "He holds a paw up to point to The Upperlands and In his other paw he holds a staff with the sigil of The Giraffe, a sign of his foresight as well as his position as a guide to others.",
        "At his feet lie two keys which are symbolic of the opening and closing of one’s mind and senses.",
        "Before him Kneel two young mice eager to learn, bearing the importance of passing on wisdom to future generations.",
    ])
    .reading([
        "Just as the Oracle acts as a guide between the known and unknown, so to is The Teacher.",
        "Though The Teacher keeps a foot planted within the solid structure of tradition and institution.",
        "You are being called to mysteries that have been discovered before but remain unknown to you.",
        "As all studies, it is imperative to have a solid foundation of the fundamentals before you can build atop them into new unknown heights.",
        "The Teacher offers understanding if you are willing to be still and listen.",
        "Now is not the time to change the script or re-invent, but instead hold to proven studies and technique.",
        "You may find yourself in the seat of The Teacher, therefore you have a responsibility to uphold the structure built by those who taught you and with it hold a generous amount of patience.",
        "Do not forget the struggle you yourself had at your humble beginnings, and impart what you learned from the many stumbles and failings along the way.",
        "Additionally, this card is an important reminder of the importance of tradition and social structures.",
        "Regardless of your feelings toward traditions, they hold valuable cultural significance within them to reflect on, and even outside rigid doctrine there is comfort in finding a like minded community to engage with.",
    ])
    .build())

define partners = (TarotCardBuilder()
    .index(6).value(6).major_arcana(True).name("The Partners")
    .keywords_upright("love, union, partnership, relationships, choices, balance, and unity")
    .description([
        "The Partners, presents two mice (A male and female) bare furred as to show their innocence and belonging within the lush nature around them.",
        "Both reaching out to one another for support.",
        "Behind the female mouse is a tree abundant with fruit, a serpent coiling its branches to caution against temptation that can lead one astray.",
        "Behind the male a burn tree stands with 12 still lit flames, suggesting the cycle of nature, that with destruction new bounties can form.",
        "Above the two mice sits the Phoenix within the clouds of the Higher Lands before the light of The Giraffe, as the mirror of The Raven it is a creature that lives in cycle of death and rebirth acting as a symbol of new beginnings and change.",
        "Hanging across its body drapes a long script, the words communicated between the two mice.",
        "Though the text may be faded, the words are not fully forgotten.",
    ])
    .reading([
        "As its namesake may imply, The Partners is a card of unity and alignment with others.",
        "Some may interpret this rather literally with the card’s design to represent sexual unions or romantic love.",
        "But, The Partners can represent togetherness in a broader sense; the support of a friend, the platonic love of family, or the sense of belonging within a community.",
        "Most importantly The Lovers reflect the value of communication, open and unashamed.",
        "Just as the mice stand bare before one another, you have to be open with those that you value within your life.",
        "There will be moments you must expose your vulnerabilities for a healthy relationship with others, but as the serpent warns, you should not only give to those who exclusively take from you.",
        "On a personal note, take to heart The Partners revealing nature for yourself, and be willing to explore yourself honestly.",
        "Communication with oneself is of equal merit as you navigate the world around you. Are you the person you wish to present to the world?",
        "Are there things you feel you must hide from those around you? Take stock of those relationships and evaluate their weight on you.",
        "Even though The Partners appreciate one's attempt to reach across the line to others, it does not mean you should allow yourself to be a victim of others' abuses.",
        "In the end, some junctions in the constant flowing river of life are meant to part.",
    ])
    .build())

define chariot = (TarotCardBuilder()
    .index(7).value(7).major_arcana(True).name("The Chariot")
    .keywords_upright("victory, success, ambition, control, determination, and self-reliance")
    .description([
        "The Chariot displays a brave warrior adorned in armor standing tall within a chariot, riding outside the walls of a fortified town, displaying them as an unshackling protector and steadfast to face the dangers of the outside world.",
        "Their armor is adorned with symbols, crescent moons for the unknown coming into view, a square upon the chest to represent the solidity and strength of their heart and spirit, and a top their laurel crown a star shines to signal their victory and change in the face of challenge.",
        "Instead of reigns the young mouse holds a wand, commanding the chariot's path not through physical effort but the strength of will.",
        "Above the charioteer waves a flag adorned with stars hung off the neck of a staff that bears the crest of The Giraffe, displaying their loyalty and connection with the celestial tapestry and the will of those above.",
        "leading the chariot are two… (ahem) “sphinx”, one white and one black, images of courage and wisdom.",
        "As they pull in two separate directions to show the conflicting paths the rider has to steer and command.",
        "All while standing tall, presenting a need to stay ready and in motion.",
    ])
    .reading(["The chariot is a card of triumph in the face of obstacles through determination and self control.",
        "Just as the warrior mouse stands tall, they appear to you to motivate you into action.",
        "Now is the time to take the reins of your own life, to push aside fear and doubt in your pursuits and goals.",
        "While it is important to draw a road map to success, you are being warned to not dwell on second guesses and the demotivational whispers of others muddying your mind.",
        "Take stock, you may find you already possess all that you need to succeed, and if not, you only need to seek the tools, likely they are more obtainable and close than you may first think.",
        "Outside of yourself The Chariot may be a call to action, that those around you are in need of your support and guidance.",
        "It may be scary to think of yourself as a leader, but your perspective and insight can prove valuable to those that are missing a piece of the puzzle.",
        "And even if you feel ill equipped for such responsibility, remember just as The Fool had their companion, and the supportive fellowship of The Partners side by side, you do not need to lead the pack to bolster a cause.",
        "You may feel like just one of many, but your efforts are a stone lain in a road toward victory.",
        "However you choose to view it, The Chariot at its core represents progress, no matter what its form may be, you should appreciate your success and achievements, no matter how big or small.",
        "You have made a step forward, and that is what is important to acknowledge and celebrate.",
    ])
    .build())

define strength = (TarotCardBuilder()
    .index(8).value(8).major_arcana(True).name("Strength")
    .keywords_upright("courage, power, confidence, compassion, and inner strength")
    .description([
        "Upon the Strength card we witness a female mouse incircled by the scaly form of a snake as it bears its fangs and rattles its tail, a symbol of clear danger and terror for mice (and most creatures I may add), as she rests her paws atop its head without fear or hesitation, her expression shows she tames the serpent not with strength or cunning, but compassion and will.",
        "The young mouse wears a white robe, a common expression for purity of spirit.",
        "An assortment of leaves and berries adorn her figure, showing her connection with the heart of nature and along with the symbol of infinity over her head, both representing her as a fertile vessel for infinite potential and wisdom.",
    ])
    .reading([
        "Much like the Chariot, the Strength card represents determination and confidence.",
        "But, while the Chariot urges a will upon the outside world around, the Strength card focuses inward on taming one's instinctual nature and emotional balance.",
        "Just like the snake would hunger to strike and the mouse's instincts to flee, your inner nature likely fights against your desired goals.",
        "This card urges you to look inward and tame your natural urges, fear, anger, anxiety.",
        "While natural to feel them, it is important to control them and not allow them to control you.",
        "Reach within yourself and summon the stamina and determination to stand composed and face the world with patience and maturity.",
        "This however is not an excuse to wear a mask.",
        "You should not let your troubles be invisible to those you care about and those who care in return, but be a strong motivator and support for them and allow them to do the same for you.",
        "Express yourself without fear, and only restrain that which may need a gentle tone.",
        "Show patience and understanding to the burdens of others, easing the weight, while being steadfast against them offloading it upon your shoulders.",
        "While you may wish to at this time be gentle and lead with care, do not lose your voice, be accretive and refuse to be trampled by the demands and expectations of others.",
        "The Strength card with all its power is here to motivate you to use your strength to control yourself more than those around you.",
        "While it is natural to feel anger, sorrow, anxiety, and fear, you have the strength and will to restrain and control them, instead of allowing them to control you.",
        "Allow yourself forgiveness for your regrets, allow yourself patience with your own shortcomings.",
        "For it is only yourself that you truly have power over, and only yourself who has power over you.",
    ])
    .build())

define hermit = (TarotCardBuilder()
    .index(9).value(9).major_arcana(True).name("The Hermit")
    .keywords_upright("introspection, contemplation, withdrawl, solitude, and self discovery")
    .description([
        "We see the Hermit, an old mouse grizzled by the wisdom of age, he stands atop a snow scraped mountain, representing his journey and growth in his solitude.",
        "He is dressed plainly in nothing but a robe, showing his detachment from materialism.",
        "Though his eyes are closed, in his right paw he holds a lantern that glows with a light symbolic of The Giraffe’s guidance within the uncertain darkness that surrounds him.",
        "In his left paw a staff, much like a wand, being the tool of the mind, showing his path is walked not by physical steps, but the stride of the soul.",
    ])
    .reading([
        "As the hermit separates himself from the follies and distractions of the outside world, so should you take a moment to connect with yourself within.",
        "Allow yourself a moment to break away from the marching pace of life and reflect on your thoughts and needs.",
        "Perhaps now is simply a good moment for a break, a quiet day to yourself, or perhaps you are in need of a vacation to collect yourself.",
        "Whatever best suits you, The Hermit reveals himself simply to remind you that now is a time to slow down, and allow yourself to get attached to the present.",
        "It is important to note that though the Hermit may seemingly walk a lonesome path, this does not demand total isolation.",
        "You may find your self reflection better spent in the presence of a like minded few, or even a self journey into a social space that holds meaning to you, such as a gallery or a coffee shop you may enjoy.",
        "All that is required is that you are given the peace of mind to allow meaningful contemplation.",
        "Additionally The Hermit may pair with cards with the intent to guide you toward relationships in need of some private report.",
        "The presence of The Empress or Emperor may nudge you toward some needed time with family, some intimate moments with someone represented by The Partners, or even the misaligned Dragons card could be urging you to better understand someone you see as an adversary in your life.",
        "No matter how The Hermits lantern may guide you, let it be one of self reflect, spiritual connection, and most importantly one grounded in the here and now.",
    ])
    .build())

define wheel_of_fortune = (TarotCardBuilder()
    .index(10).value(10).major_arcana(True).name("The Wheel of Fortune")
    .keywords_upright("good luck, change, cycles, decisive moments, fortune, and turning points")
    .description([
        "Within the confines of The Wheel we observe a mouse running within its frame, at its center there is a circle with a dot, a sigil that represents the sun and the central power of The Giraffe, branching out from the sun are the eight signs of the planets that make their cycles around the sun.",
        "Extending from the cardinal directions of the center of the wheel are the four arrows that represent the elements earth, fire, air and water along with the balance of nature and its seasons.",
        "Along the outer ring of the wheel’s circumference are inscribed the 12 zodiac signs, another representation of the cycles of the year along with the coming of new life in birth.",
        "Encircling the wheel a serpent bites its tail, an ouroboros, a common image of the cycles of nature, life, death, and rebirth within eternity, this serpent's path acts against the mouse's stride, acting as a constant resistance to their progress.",
        "Above the wheel The Giraffe and a Dragon watch the mouse, acting as observers to the mouse’s struggles and progress, giving no more than guidance outside the mouse’s confined world from opposing sides.",
        "Below we see two animals, a male and female, seemingly unaware of the mouse.",
        "The female is beautiful and green furred, acting as an image of femininity and fertility. The Male is more greyed with age and worldly experience.",
        "The two figures read from books, expanding their wisdom and experience of the world, but also distracted from the struggles of the mouse’s infinite journey.",
    ])
    .reading([
        "The Wheel in essence is the symbol of cycles and the inevitable inertia of life.",
        "Know that in times of strife and struggle, eventually a rugged path will smooth, and inversely in times of good fortune, so too will the high path eventually dip.",
        "Regardless the road your journey currently is on, The Wheel reminds you that there is no path but forward you just have to choose to keep moving.",
        "Just as the mouse runs within the wheel, there may be many things that act against you, it is only through perseverance will you meet your goal, but just like the animals who surround the mouse within this card, you are reminded that you are not alone along these winding roads.",
        "While they may not be fully aware of your burden, you equally are ignorant of theirs.",
        "The people met at these cross roads should be thought of as opportunities to lift one another up above the surface of rising tides.",
        "The Wheel is notably one of the most subjective and symbolic card within the deck, decorated with glyphs and characters that note the repeated cycles of the world around us.",
        "Days, months, years, from seasons, to celestial alignments, the very universe ticks around us in a natural clockwork.",
        "Take head of the important moments that come and go and come again.",
        "Simple gestures of birthdays and holidays, whether you appreciate the steeping of tradition or not, hold significance and should be recognized and remembered as a chapter in one's own story.",
        "And as its name sake implies, The Wheel is a card of luck and good fortune.",
        "With this card present you can be assured that prosperity and reprieve are certainly around the corner.",
        "Though the Wheel still represents effort and momentum, it is not always best to sit and wait for your good fortune to arrive, at times it is best to take the wheel into your own hands, be decisive and act with solid intention and guidance, and you should be able to craft your own luck.",
    ])
    .build())

define justice = (TarotCardBuilder()
    .index(11).value(11).major_arcana(True).name("Justice")
    .keywords_upright("justice, karma, accountability, fairness, truth, cause and effect, and law")
    .description([
        "The figure of Justice sits before a loose purple veil, a color of wisdom, creativity, and often the power of royalty or nobility.",
        "The veil hangs between two pillars, much like that of the Oracle and Teacher they represent order and structure.",
        "In the mouse’s right paw she holds up a double edged sword, showing her authority and decisiveness, the double edged blade a reminder of the consequences our actions and decisions hold.",
        "In her left paw, hangs a pair of scales, balanced to symbolize her impartiality and sense of logic.",
        "Atop her head rests a crown with a diamond set in the center to represent her clarity of mind, along with the golden mantle draping her shoulders to represent her authority of The Giraffe’s will.",
        "Though, from under her red robes, a color of power and strength, a bare foot peaks out, not only as a sign of her spiritual purity, but a reminder of her humility and position down on earth alongside any other animal.",
    ])
    .reading([
        "The karmic balance of the Justice card calls to those in need of reflection of their actions and consequences.",
        "Whether past, present, or future, the choices you have or will make are in need of deep introspection.",
        "Perhaps there are acts in your past that you have buried or put to the side of your conscience thoughts that are in need of resolution, damage you have left to smolder can not be built on top of without first clearing what was left behind.",
        "Inversely, you may currently be at a crossroad in your journey that may be significant to your distant destination, if not now surely this choice is soon to come.",
        "Justice wishes you to make your choices clear, with logic and patience.",
        "Now is not the time for fantastical flights or haphazard decisions, as their outcomes could be long lasting and drastic.",
        "If your focus on this card is outside yourself, Justice bares a sword for a decisive strike of karma to the world around you.",
        "If you have been wrong, she will act as your guide to correct what has been done with compassion, reason, and integrity.",
        "If the world is in disorder, she is a sign of the coming hammer of order.",
        "Regardless of the reason it is important to keep in mind that you must be an active participant in correcting the disharmony you live in, for she can only grant you the tools to balance the scales.",
    ])
    .build())

define hanged_mouse = (TarotCardBuilder()
    .index(12).value(12).major_arcana(True).name("The Hanged Mouse")
    .keywords_upright("sacrifice, pause, surrender, letting go, and new perspectives")
    .description([
        "A mouse hangs suspended from a natural T-shaped growth of wood and foliage by their tail, hanging upside down to gain a new perspective, their expression calm and posture relaxed showing that they are in this position by their own choosing and the lack of any bindings, they restrain themself by their own will.",
        "The mouse dawns no clothing, both to free themselves of the burden of material distractions and to connect themselves with their primal natural state.",
        "Around their head a halo of light glows, expressing a new insight and awareness, along with the enlightenment that brings them closer to The Giraffe.",
    ])
    .reading([
        "The Hanged Mouse most often reveals themselves to those who have become encumbered by life’s many forked paths and innumerable possibilities.",
        "You may be juggling too many hobbies, or perhaps there is simply a list of todo’s that continues to grow.",
        "regardless of  your desire or the demands of your environment there might just seem too much to do and too little time.",
        "The Hanged Mouse calls to remind you to slow down and take some time to unpack the burdens you carry, and if not by your choosing, life will find a way to do it for you in ways as unfortunate as they are poorly timed.",
        "As such it is important to find your moments to rest, allow yourself a brief window to go with the flow, and give yourself some time to sort the necessities from desires.",
        "Organize what must be done, from the things that can be delayed, while it may be difficult, sometimes things simply need to be put on the shelf until a time you can give it the proper attention it needs.",
        "And while painful, sometimes it is more reasonable to let things that you have carried for too long go.",
        "The Hanged Mouse, much like the Fool, is a sign of a free spirit in need of new perspectives and experiences.",
        "Just as the Hanged Mouse views the world inverted, now may be a much needed time for you to turn your view of the world around.",
        "In your breaks and rest perhaps you should try something new, wander trails you have previously avoided, or simply return to something that has been left on that shelf in need of a new fresh perspective filled with much needed experience.",
        "Regardless of how you view this card, note that the restraints that hold you back are merely your own, and you choose how to perceive them.",
    ])
    .build())

define death = (TarotCardBuilder().description([
    "The Giraffe holds the sun high into the sky with radiants of its straight, optimism and revealing light, from behind a brick wall four sunflowers sprout and reach over their barricade unrestrained, the four flowers representing the growth and connection with nature, the four suits of the minor arcana and the elements they encapsulate.",
    "In front of the wall illuminated by the sun is a small mouse, bare furred and freely expressing themselves in every spectrum the light grants to them, they joyfully ride a white hobby horse, showing their purity and youthful spirit free from concern, self doubt, or judgment.",
])
    .index(13).value(13).major_arcana(True).name("Death")
    .keywords_upright("endings, change, transformation, transition, and letting go")
    .description([
        "Within the death card we see the image of The Raven, the avatar of death and passing, the messenger of the after life and the carrier of souls beyond the veil.",
        "It appears as a skeletal figure to show all that remains of the mortal body after the soul has left, its figure nothing more than a dark void to reflect its connection to the unknown of the other side.",
        "At the Raven’s foot lies a royal figure to be carried away, representing the passing of generations along with their dominion.",
        "Before the Raven a mouse pleads to be spared, but its inured gaze offers no pity, telling us that no creature is granted reprieve from the inevitable.",
        "The Raven carries with it a white rose, a symbol of purity, innocence and new beginnings.",
        "While death may be painful it also does not judge or bare malice and can also be the start of a new chapter towards something beautified if acknowledged and learned from.",
        "In the background we can see a boat filled with celebrating mice sails down a river toward the setting sun, a sign they follow the path of the giraffe, toward a golden city beyond a gate of two towers that bare a striking resemblance to the ones present in the moon card, a hint of the unknown that abates them on the other side of their journey.",
    ])
    .reading([
        "Despite its name sake and misinterpretations, the Death card is not a representation of literal death (Though it is not excluded either), but at its core death is the harbinger of swift, unbiased, and inevitable change.",
        "Aside its negative perceptions, the Death card is possibly one of the most positive cards within the deck, signaling an end point to a major phase in your life and now find yourself in the transitional seas of possibility, and while the currents may be calm of turbulent you now have an open view for a new destination in your life’s path.",
        "You are being given an opportunity to sway the path you were on to new and brighter destinations, the chance to reinvent yourself, and find a brighter destination.",
        "It is important to realize though that the key to the Death cards positive outcomes is the need to let go of the elements of the previous phase in your life that did not serve to better you.",
        "In many ways these changes in life can be as small as acknowledging a healthier diet after a brief medical scare, or as large as a sudden loss of a loved one.",
        "Regardless of the call, The Death card will make the message known and it will be up to you how you respond to it.",
        "Regarding loss however, there is no shame in mourning the loss of something (especially some one) significant in your life.",
        "This card nearly wants to gently remind you that such pain should only be allowed to be temporary.",
        "Cherish the lessons learned and the times that were bright, but be willing to let go and move forward.",
        "For there is nothing those who have passed on would regret more, than looking back and witnessing a sinking ship…",
    ])
    .build())

define temperance = (TarotCardBuilder()
    .index(14).value(14).major_arcana(True).name("Temperance")
    .keywords_upright("balance, moderation, patience, and tranquility")
    .description([
        "Temperance takes the form of a feminine figured angel who bares the wings of Aries, The Ram of war and conflict, showing them to be between the words of the feminine and masculine.",
        "They balance one foot on a rock and the other dipped into the flowing waters of a river, keeping themselves between a grounded state and one with the flow of the turbulence of nature.",
        "They pour water between two cups to express the flow of life.",
        "Behind the angel a winding road leads up a mountain towards The Giraffes guiding light, symbolizing ones need to stay true to when walking journey toward their purpose.",
    ])
    .reading([
        "Temperance is a card that beckons you to bring moderation and balance into your pursuits.",
        "In her presence you likely already have your destination well within sight and are only in need of fine tuning to complete your journey.",
        "You are being signalled to continue with patience and consideration of your options.",
        "While it may seem like the choices are black and white, Temperance reminds you that there is always a middle ground to the nuances of life.",
        "Temperance also acts as a guide to moderating your life's pleasures and obligations, tilting the scales to one extreme or the other can easily end in equal pits of despair.",
        "Please recognize though that moderation does not mean strict abstinence, to avoid is an act of fear, it is better to control these aspects of your life than to allow them to control you.",
        "Most importantly, temperance reflects on your inner growth and recognition, both body and mind need to be tempered for true balance.",
        "Take the time needed to hone your crafts and the little victories needed to bolster your confidence, as you can not grow if you can not see yourself able.",
    ])
    .build())

define dragons = (TarotCardBuilder()
    .index(15).value(15).major_arcana(True).name("The Dragons")
    .keywords_upright("oppression, attachment, addiction, excess, restriction, and sexuality")
    .description([
        "As The Story of the Dragons, we are shown the Green Dragon; The betrayer and the betrayed, the truthful liar, and the imprisoned free spirit.",
        "She sits atop a pedestal, wingless, bound by her neck with a heavy chain.",
        "Before the dragon two mice, a male and female, stand also bound to the pedestal by golden threads, a symbol of the attachment of the physical and spiritual as well as ethereal guidance.",
        "They are both bare furred, their tails ending with a bushel of grapes and a flame, representing their attachment to their primal instincts through lust and pleasure.",
        "While the two mice appear to be bound, at a closer glance one can see the threads are loose and nearly tied with a simple knot, revealing they are held more by their own choice than any force.",
        "Behind the dragon there is a pentalpha roughly drawn, both a symbol of geometric prowess and magical knowledge, but a commonly used mark of protection, representing the tempting offers she had made.",
    ])
    .reading([
        "Like the dragon you have had your wings clipped, you are likely feeling bound in some way to a negative aspect of your life.",
        "This car often reflects much on your inner struggles to progress, to let go of negative emotions, or cut ties with toxic influences that impose upon you.",
        "If reflecting on this card from within, you may be listening too much to an inner voice not your own.",
        "Or perhaps like the dragons you have grown materialistic and overly attached to the physical possessions you feel give you meaning and value.",
        "Or, worse still you may be caught in the jaws of one of your pleasurable vices.",
        "Externally, a dragon figure in your life may be hindering you from your path.",
        "This could be an image of The Partners in your life flipping to the inverted, you may feel shackled into a career that does not suit you, or even the pressures of societal expectations are baring down on you.",
        "No matter the source, you should recognize that you are not the dragon held by chains, but the mouse, collared by nothing more than loose string that merely suggests their stay.",
        "While these figures may feel necessary and at times valued in your day to day existence, it is imperative that you weigh their value to your own pursuits and goals, and always remember that no matter how tight the line may feel you are the only one who holds the tools to your own freedom.",
    ])
    .build())

define tower = (TarotCardBuilder()
    .index(16).value(16).major_arcana(True).name("The Tower")
    .keywords_upright("destruction, trauma, upheaval, chaos, and awakening")
    .description([
        "We bear witness to a chaotic scene of a tower perched at the peak of a jagged mountain with a crown atop its roof, a symbol of pride and structure on a solid foundation, as a bolt of lightning strikes the crown from its top and engulfs the spire in flames.",
        "This tragedy is quick and unexpected, upheaving the lives of its occupancy as we see a mouse leaping from the window into the unknown perils below.",
    ])
    .reading([
        "Much like the Death card, The Tower is a forewarning of significant change, however the Tower card embodies an upheaval of one's old way on a foundational level.",
        "Like the tower itself, something within you or your life has been crafted on faulty unstable grounds and it will take but a single sharp strike to crumble.",
        "This card often reflects significantly on one's old presuppositions, traditions, or even religious views.",
        "When applying the Towers message in retrospect, it could symbolize the need to come to terms with old values that have worn out and lost their significance in your life, or to reconcile the lasting effects of trauma you have ignored.",
        "Regardless of past or present, The Tower will tend in the way of your journey, and is a waypoint you will have to navigate with a slow and tentative pace.",
        "Recognize that it is ok to take a moment's rest and collect the broken pieces and consider what is worth salvaging if possible.",
        "Take heart that while this may be a difficult step, it does not have to be a wholly negative stage of your life, you could not build on the fragile old structure you had, and now you have the opportunity to start anew with a more stable footing.",
    ])
    .build())

define stars = (TarotCardBuilder()
    .index(17).value(17).major_arcana(True).name("The Stars")
    .keywords_upright("hope, inspiration, positivity, faith, and renewal")
    .description([
        "Within The Star card we see a nude mouse, though bare furred she is perfectly relaxed out in the vast world around her, showing her innocence, vulnerability and connection with the natural world.",
        "She stands one foot on land and the other into the water, representing her balance between the practical sense of the world and the openness to the intuitive spirit of the ethereal plane.",
        "In her paws she holds two jugs that pour water, one into the waters expressing her abundant flow of wisdom, and one onto the land which sprouts flowers from her care and nurturing.",
        "Behind her The Phoenix, a symbol of life and healing, rests atop a tree to remind us the importance of taking time to rejuvenate one’s mind and body.",
        "Among the stars in the background The Giraffe can be seen on the horizon, a sign of the approaching light of the sun to bring another day.",
    ])
    .reading([
        "Just as the mouse of this card, you have relinquished much and have likely faced some recent hardship and made it to the other side of a hazardous road. Or, if you currently find yourself among such hardships, The Stars grant you a guiding light to reach.",
        "For now, allow the distant light of The Star be a beacon of hope and a reminder that another day comes with new potential.",
        "For now you are resting in the liminal space of your old self and an entirely new you, as such now is a good opportunity to look toward the veil above and recognize how small you are, but how vast your potential remains to be and how much you still have to offer to the world around you.",
        "Reflect on the myriad of lives and perspectives around you, each a solar system of their own that signals to one another with brief twinkles and their gravitational pull.",
        "You like the stars are one of billions, but just like the flow of the cosmos, the billions of you form something so much more.",
    ])
    .build())

define moon = (TarotCardBuilder()
    .index(18).value(18).major_arcana(True).name("The Moon")
    .keywords_upright("illusions, secrets, uncertainty, intuition, and the subconscious")
    .description([
        "The moon hangs suspended affront a black void, it takes the image of a seemingly innocent and pure white rabbit - an animal of luck, fertility, and good fortune to many, but to some folklores a mischievous trickster that may not be all that it appears - curled up in rest, dreaming of imagined worlds.",
        "She hangs between two towers, ones similar to the far lands of the death card, acting as the gates to a land unknown, a long road winding into an uncertain destination in the distance devoid of the guiding light of The Giraffe.",
        "In the fields mice scurry and hide, as is their instinctual nature, before the enigmatic figure of The Moon, anxious of its hidden intentions.",
        "Though at the start of the path a mouse stands bold in her light, bravely gazing upon her and the path she leads.",
        "The trailhead opens into a small pond symbolizing the boundaries of the material and ethereal planes, as two koi, one white and one black, swim around one another, expressing the entertaining of opposites and their inevitable cycles with one another.",
    ])
    .reading([
        "Just as the Rabbit may hide its true nature, so too may things not be all they seem to be.",
        "Like the pull of the moon on the tides, invisible threads influence you now.",
        "Questions linger unanswered and your path may be obscured to you at this stage of your travels.",
        "If you choose to look inward, The Moon looms over your anxieties and insecurities.",
        "You may not even be fully aware of what weighs on you, but its gravity is significant all the same.",
        "You may wish to meditate on deeper thoughts you are not allowing yourself to fully contemplate.",
        "Perhaps your mind is already doing so through dreams, if so then you should attempt to pull them forward into your conscious mind.",
        "If the light of the moon shines from outside the windows of your internal self, then you may be questioning the intentions of those around you.",
        "It is fair to trust your senses, but don’t allow your intuition to overcome your judgement.",
        "There is often good reason others to keep their secrets, it may be best to allow others their private thoughts while remaining cautious of manipulation.",
        "Either way, The Moon wishes to shine clarity not on the external sources of your concerns but to illuminate why you have these turbulent thoughts and feelings churning deep inside yourself.",
        "Use your intuition and be mindful of your interactions with others you surround yourself with, though be aware that others may be just as in the dark as you and that a dark road can not be safely traveled without first lighting the way.",
    ])
    .build())

define sun = (TarotCardBuilder()
    .index(19).value(19).major_arcana(True).name("The Sun")
    .keywords_upright("happiness, success, optimism, vitality, confidence, and truth")
    .description([
        "The Giraffe holds the sun high into the sky with radiance, optimism, and revealing light.",
        "from behind a brick wall four sunflowers sprout and reach over their barricade unrestrained, the four flowers representing the growth and connection with nature, the four suits of the minor arcana and the elements they encapsulate.",
        "In front of the wall illuminated by the sun is a small mouse, bare furred and freely expressing themselves in every spectrum the light grants to them.",
        "They joyfully ride a white hobby horse, showing their purity and youthful spirit free from concern, self doubt, or judgment.",
    ])
    .reading([
        "The light of The Sun dawns to illuminate your path and reveal your inner truths.",
        "You may have goals or thoughts that are now coming into focus, and if not yet they are soon to come clear to you.",
        "The road is bright and in view, the lines on the map are drawn, and now is your time to reach for what you have worked toward.",
        "The sun may also be a sign to allow yourself to reveal your inner most truths and sincere self to the world.",
        "Let your true persona radiate vibrantly with optimism and pride, your inner light could well be the beacon others around you are in need of to brighten their path.",
        "Lastly, you are reminded The Giraffe looks over all equally and offers shade to those that are exposed most harshly to the Sun’s rays.",
        "Have faith in the communities you walk.",
        "While some may not grant you the same kindness, for it is through patience and understanding may one not be blinded by the rising sun.",
    ])
    .build())

define judgement = (TarotCardBuilder()
    .index(20).value(20).major_arcana(True).name("Judgement")
    .keywords_upright("judgment, rebirth, self evaluation, awakening, purpose, and absolution")
    .description([
        "We pear over a field of graves, as mice - male, female, young and old alike, rise from their graves to the trumpeting call of The Ram, a symbol of strength, courage and sacrifice, Aries, the deific animal of conflict, strife, and the fall and rise of empires.",
        "The Ram blows into his own severed horn, to show humility even at his rank, his billowing call across the land an order to all passing on to come forth for judgment.",
        "The Ram floats over a high reaching mountain range, to represent the insurmountable challenges we face through our journeys before our inevitable call.",
    ])
    .reading([
        "You are being beckoned to take account for your actions and the karma of your inner intentions.",
        "Judgement calls to those in need of self reflection of one’s past deeds, as well as a signalling of the repercussions to come.",
        "Depending on your situation this card can be either a a welcomed sight or a cause for alarm.",
        "For some this could mean that events in their past have not been fully acknowledged, feelings left unreconciled, or old tasks left undone.",
        "Take stock of the weight that has accumulated on your soul.",
        "Both the long forgotten whispers of the past that echo to you, or a closer more recent shout fills your mind, you are being forced to confront these anxieties.",
        "Ask yourself if you have the means to confront what must be done, can you let it go and leave it behind, or is it worth holding onto as a means to remember and better yourself?",
        "For others, you may have been wronged, and Judgement wishes to assist in renewing the balance of the scales.",
        "Whether it be the minor conflict, or the deeps scars of trauma left by the cruel actions of some one you crossed path with in your life's journey, you must choose your actions to make amends or let it fester.",
        "Regardless of your own actions however, anothers path carries their own billowing call eventually.",
        "However if these acknowledgments feel familiar and recent, then this card comes with recognition that you have faced your trials and will soon be met by the inevitable consequences to come for those deemed guilty.",
    ])
    .build())

define world = (TarotCardBuilder()
    .index(21).value(21).major_arcana(True).name("The World")
    .keywords_upright("completion, integration, fulfillment, travel, wholeness, and harmony")
    .description([
        "We witness a mouse at the end of her journey, bare furred she prances through the open mouth of a large laurel wreath with a red scarf dancing around her form, all to represent her passing from one stage to the next in proud victory.",
        "While she moves forward, she gazes back, a smile on her face in reflection of the challenges and lessons learned that brought her here now.",
        "In her paws she carries two wands like that of the magician, signaling that her desires and goals have become manifest through her will and new found knowledge and skill.",
        "Around the wreath the four figures from The Wheel are present, tying the nature of the two cards firmly together, as one journey ends a new one begins.",
        "The figures around the mouse now all observe her, having become active agents of her narrative and fully recognized parts of each other's shared world.",
    ])
    .reading([
        "You have walked a long road, faced trials and hardship, and embraced the inevitability of change.",
        "The Word stands before you as a goalpost to the end of your journey, a path well traveled with its lessons taken to heart.",
        "Now you have passed into a point of accomplishment, if not yet, then soon to be met.",
        "In a sense the world card tells you that you have passed a milestone in your life and have come to terms with all that the future entails and expects of you.",
        "If looking towards the future, then there are changes to come that will bring you wholeness and a sense of fulfillment.",
        "Either way, you are being told to be open to what comes and go with the flow of the world around you to find harmony.",
        "Additionally The World is a card of community and togetherness, try and give as much as you take, to listen and much as you speak.",
        "The World's gravity pulls at you, and draws all things together.",
        "Be open to the lives that come and go, passing in your travels, reflect on their impact on you and your impact on them and you will acknowledge that we are all connected within the grand tapestry.",
    ])
    .build())
