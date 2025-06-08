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

        def upright(self, upright):
            self.card.upright = upright
            return self

        def reversed(self, reversed):
            self.card.reversed = reversed
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
            self.major_arcana = None
            self.name = None
            self.upright = None
            self.reversed = None
            self.reading = ["It means...", "Errr...", "Uhhhm...", "I forgot...", "...", "Oh well!"]
            self.inv_reading = ["It means...", "Errr...", "Uhhhm...", "I forgot...", "...", "Oh well!"]


    ### My Functions ###

    def coin_flip():
        for x in range(5):
            c = int(renpy.random.choice(list(range(100))))

        if c >= 50:
            return False
        else:
            return True

    def long_reader(character, card_info):

        lines = card_info
        index = 0

        while index < len(lines):
            line = lines[index]
            renpy.say(character, line)
            index += 1
            
# Define all cards
define fool = (TarotCardBuilder()
    .index(0).value(0).major_arcana(True).name("The Fool")
    .upright("Beginning, Innocence, Spontaneity, and A free spirit")
    .reversed("Holding back, Recklessness, and Risk-taking")
    .reading(["The Fool is the card of wanderers and adventure.",
    "Just as The Fool, you are on the precipice of uncertainty and gazing into the unknown potential of what lies ahead.",
    "Now is a good time for something new, to take that risky step into the uncertain.",
    "Perhaps your anxieties are restraining your thoughts and willingness to move forward, but just like The Fool, you should set aside the fears and think of not only what you have to potentially lose, but more importantly what you may fail to gain.",
    "Though be sure to look before you leap. Just because you should have the courage to embrace the new, you should also be aware of the very real risk that may lie within.",
    "After all, there is a big difference between naivety and simple pure foolishness."])
    .inv_reading(["Just as the Fool represents potential and the possible, it can equally be a warning of your own ability to limit that potential.",
    "Inverted The Fool acts as a messenger of your self imposed limitations.",
    "Perhaps your anxieties or fears have left you unwilling to act, or maybe you are overwhelmed by the limitless possibilities that can go wrong.",
    "Either way, you have something you desire and you have restrained yourself from achieving it, or possibly from even taking the first step.",
    "It is ok to slow down and take stock of these ideas and desires, you need to allow yourself to unpack and analyze the why and how to achieve your goals.",
    "I suggest perhaps you make a list of the pro’s and con’s.",
    "It is important to remember that this representation is only the opposite side to the same beginning as The Fool’s upright meaning, as some adventures are not so spontaneous, and you need to know where to go to eventually arrive there.",
    "But, in the end, you are the only one who can shackle yourself into stagnation, and it is upon you to free yourself of that weight."])
    .build())

define magician = (TarotCardBuilder()
    .index(1).value(1).major_arcana(True).name("The Magician")
    .upright("Willpower, Desire, Creation, and Manifestation")
    .reversed("Trickery, Illusion, and Out of Touch")
    .build())

define high_priestess = (TarotCardBuilder()
    .index(2).value(2).major_arcana(True).name("The High Priestess")
    .upright("Intuition, The Unconciouse, and Inner Voice")
    .reversed("Lack of Balance, Silencing, and Repressed Feeling")
    .build())

define empress = (TarotCardBuilder()
    .index(3).value(3).major_arcana(True).name("The Empress")
    .upright("Motherhood, Fertility, and Nature")
    .reversed("Dependence, Smothering, and Emptiness, Nosiness")
    .build())

define emperor = (TarotCardBuilder()
    .index(4).value(4).major_arcana(True).name("The Emporer")
    .upright("Authority, Structure, Control, and Fatherhood")
    .reversed("Tyranny, Rigidity, and Coldness")
    .build())

define teacher = (TarotCardBuilder()
    .index(5).value(5).major_arcana(True).name("The Teacher")
    .upright("Tradition, Conformity, and Morality, Ethics")
    .reversed("Rebellion, Subversion, and New Approach")
    .build())

define partners = (TarotCardBuilder()
    .index(6).value(6).major_arcana(True).name("The Partners")
    .upright("Partnership, Duality, and Union")
    .reversed("Unbalanced, One Sidedness, and Disharmony")
    .build())

define chariot = (TarotCardBuilder()
    .index(7).value(7).major_arcana(True).name("The Chariot")
    .upright("Direction, Control, and Willpower")
    .reversed("Loss of Control, Lacking Direction, and Aggression")
    .build())

define strength = (TarotCardBuilder()
    .index(8).value(8).major_arcana(True).name("Strength")
    .upright("Confidence, Courage, Compassion, and Focus")
    .reversed("Self Doubt, Weakness, and Insecurity")
    .build())

define hermit = (TarotCardBuilder()
    .index(9).value(9).major_arcana(True).name("The Hermit")
    .upright("Contemplation, Seeking Truth, and Guidance")
    .reversed("Loneliness, Isolation, and Lost Path")
    .build())

define wheel_of_fortune = (TarotCardBuilder()
    .index(10).value(10).major_arcana(True).name("The Wheel of Fortune")
    .upright("Change, Cyclicle, and Inevitability")
    .reversed("Lack of Control, Desperation, and Misfortune")
    .build())

define justice = (TarotCardBuilder()
    .index(11).value(11).major_arcana(True).name("Justice")
    .upright("Cause and Effect, Clarity, and Truth")
    .reversed("Dishonesty, Unaccountability, and Iniquity")
    .build())

define hanged_mouse = (TarotCardBuilder()
    .index(12).value(12).major_arcana(True).name("The Hanged Mouse")
    .upright("Sacrifice, Release, and Altruism")
    .reversed("Hesitation, Needless Loss, and Constraint")
    .build())

define death = (TarotCardBuilder()
    .index(13).value(13).major_arcana(True).name("Death")
    .upright("End of a Cycle, New Beginings, Change, and Metamorphosis")
    .reversed("Fear of Change, Stasis, Stagnation, and Decay")
    .build())

define temperance = (TarotCardBuilder()
    .index(14).value(14).major_arcana(True).name("Temperance")
    .upright("The Middle Path, Patience, and Finding Purpose")
    .reversed("Extremes, Excess, and Imbalance")
    .build())

define dragons = (TarotCardBuilder()
    .index(15).value(15).major_arcana(True).name("The Dragons")
    .upright("Addiction, Materialism, and Miscreance")
    .reversed("Freedom, Release, and Regaining Control")
    .build())

define tower = (TarotCardBuilder()
    .index(16).value(16).major_arcana(True).name("The Tower")
    .upright("Upheaval, Broken Pride, and Disaster")
    .reversed("Avoiding Tragedy, Delayed Disaster, and Fear of Suffering")
    .build())

define stars = (TarotCardBuilder()
    .index(17).value(17).major_arcana(True).name("The Stars")
    .upright("Hope, Faith, and Rejuvination")
    .reversed("Lacking Faith, Discouragment, and Insecurity")
    .build())

define moon = (TarotCardBuilder()
    .index(18).value(18).major_arcana(True).name("The Moon")
    .upright("Unconciousnes, Illusions, and Intuition")
    .reversed("Confusion, Fear, and Misinterpretation")
    .build())

define sun = (TarotCardBuilder()
    .index(19).value(19).major_arcana(True).name("The Sun")
    .upright("Joy, Success, Celebration, and Positivity")
    .reversed("Negativity, Depression, and Sorrow")
    .build())

define judgement = (TarotCardBuilder()
    .index(20).value(20).major_arcana(True).name("Judgement")
    .upright("Reflection, Reckoning, and Awareness")
    .reversed("Lacking Self Awareness, Doubt, and Self Loathing")
    .build())

define world = (TarotCardBuilder()
    .index(21).value(21).major_arcana(True).name("The World")
    .upright("Fulfillment, Harmony, and Completion")
    .reversed("Incompletion, Failure, and Lack of Closure")
    .build())

define ace_of_wands = (TarotCardBuilder()
    .index(22).value(1).major_arcana(False).name("Ace of Wands")
    .upright("Creation, Willpower, Inspiration, and Desire")
    .reversed("Lacking Energy, Lack of Passion, and Boredom")
    .build())

define two_of_wands = (TarotCardBuilder()
    .index(23).value(2).major_arcana(False).name("2 of Wands")
    .upright("Planning, Making Decisions, and Leaving Home")
    .reversed("Fearing Change, Playing it Safe, and Bad Planning")
    .build())

define three_of_wands = (TarotCardBuilder()
    .index(24).value(3).major_arcana(False).name("3 of Wands")
    .upright("Looking Ahead, Expansion, and Rapid Growth")
    .reversed("Obstacles, Delay, and Frustration")
    .build())

define four_of_wands = (TarotCardBuilder()
    .index(25).value(4).major_arcana(False).name("4 of Wands")
    .upright("Community, Home, and Celebration")
    .reversed("Lacking Support, Transience, and Home Conflicts")
    .build())

define five_of_wands = (TarotCardBuilder()
    .index(26).value(5).major_arcana(False).name("5 of Wands")
    .upright("Competition, Rivalry, and Conflict")
    .reversed("Avoiding Conflict, and Respecting Differences")
    .build())

define six_of_wands = (TarotCardBuilder()
    .index(27).value(6).major_arcana(False).name("6 of Wands")
    .upright("Victory, Success, and Accolades")
    .reversed("Pride, Lacking Recognition, and Punishment")
    .build())

define seven_of_wands = (TarotCardBuilder()
    .index(28).value(7).major_arcana(False).name("7 of Wands")
    .upright("Perseverance, Defense, and Maintaining Control")
    .reversed("Give Up, Loss of Confidence, and Overwhelmed")
    .build())

define eight_of_wands = (TarotCardBuilder()
    .index(29).value(8).major_arcana(False).name("8 of Wands")
    .upright("Swift Action, Movement, and Quick Decisions")
    .reversed("Panic, Wait, and Slowdown")
    .build())

define nine_of_wands = (TarotCardBuilder()
    .index(30).value(9).major_arcana(False).name("9 of Wands")
    .upright("Resilience, Grit, and Last Stand")
    .reversed("Exhaustion, Fatigue, and Questioning Ones Motivations")
    .build())

define ten_of_wands = (TarotCardBuilder()
    .index(31).value(10).major_arcana(False).name("10 of Wands")
    .upright("Accomplishment, Responsibility, and Burden")
    .reversed("Inability to Delegate, Overstressed, and Burnt Out")
    .build())

define page_of_wands = (TarotCardBuilder()
    .index(32).value(11).major_arcana(False).name("Page of Wands")
    .upright("Freedom, Exploration, and Excitment")
    .reversed("Lacking Direction, Procrastination, and Creating Conflict")
    .build())

define knight_of_wands = (TarotCardBuilder()
    .index(33).value(12).major_arcana(False).name("Knight of Wands")
    .upright("Action, Adventure, and Courage")
    .reversed("Anger, Impulsiveness, and Recklessness")
    .build())

define queen_of_wands = (TarotCardBuilder()
    .index(34).value(13).major_arcana(False).name("Queen of Wands")
    .upright("Courage, Determination, and Joy")
    .reversed("Selfishness, Jealousy, and Insecurity")
    .build())

define king_of_wands = (TarotCardBuilder()
    .index(35).value(14).major_arcana(False).name("King of Wands")
    .upright("The Big Picture, Leadership, and Overcoming Challenges")
    .reversed("Impulsive, Overbearing, and Unachievable Expectations")
    .build())

define ace_of_cups = (TarotCardBuilder()
    .index(36).value(1).major_arcana(False).name("Ace of Cups")
    .upright("New Feelings, Spirituality, and Intuition")
    .reversed("Emotional Loss, Blocks Creativity, and Emptiness")
    .build())

define two_of_cups = (TarotCardBuilder()
    .index(37).value(2).major_arcana(False).name("2 of Cups")
    .upright("Unity, Partnership, and Connection")
    .reversed("Immbalance, Broken Communication, and Tension")
    .build())

define three_of_cups = (TarotCardBuilder()
    .index(38).value(3).major_arcana(False).name("3 of Cups")
    .upright("Friendship, Community, and Happiness")
    .reversed("Overindulgence, Gossip, and Isolation")
    .build())

define four_of_cups = (TarotCardBuilder()
    .index(39).value(4).major_arcana(False).name("4 of Cups")
    .upright("Apathy, Contemplation, and Disconnectedness")
    .reversed("Sudden Awareness, Choosing Happiness, and Acceptance")
    .build())

define five_of_cups = (TarotCardBuilder()
    .index(40).value(5).major_arcana(False).name("5 of Cups")
    .upright("Loss, Grief, and Self Pity")
    .reversed("Acceptance, Moving On, and Finding Peace")
    .build())

define six_of_cups = (TarotCardBuilder()
    .index(41).value(6).major_arcana(False).name("6 of Cups")
    .upright("Familiarity, Happy Memories, and Healing")
    .reversed("Moving Forward, Leaving Home, and Independence")
    .build())

define seven_of_cups = (TarotCardBuilder()
    .index(42).value(7).major_arcana(False).name("7 of Cups")
    .upright("Searching for Purpose, Choices, and Daydreaming")
    .reversed("Lack of Purpose, Diversion, and Confusion")
    .build())

define eight_of_cups = (TarotCardBuilder()
    .index(43).value(8).major_arcana(False).name("8 of Cups")
    .upright("Walking away, Disillusionment, and Leaving Behind")
    .reversed("Avoidance, Fearing Change, and Fear of Loss")
    .build())

define nine_of_cups = (TarotCardBuilder()
    .index(44).value(9).major_arcana(False).name("9 of Cups")
    .upright("Satisfaction, Emotional Stability, and Luxury")
    .reversed("Lack of Inner Joy, Smugness, and Dissatisfaction")
    .build())

define ten_of_cups = (TarotCardBuilder()
    .index(45).value(10).major_arcana(False).name("10 of Cups")
    .upright("Inner Happiness, Fullfillment, and Dreams Coming True")
    .reversed("Shattered Dreams, Broken Family, and Domestic Disharmony")
    .build())

define page_of_cups = (TarotCardBuilder()
    .index(46).value(11).major_arcana(False).name("Page of Cups")
    .upright("Happy Surprise, Dreamer, and Sensitivity")
    .reversed("Emotional Immaturity, Insecurity, and Disappointment")
    .build())

define knight_of_cups = (TarotCardBuilder()
    .index(47).value(12).major_arcana(False).name("Knight of Cups")
    .upright("Following the Heart, Idealist, and Romantic")
    .reversed("Moodiness and Disappointment")
    .build())

define queen_of_cups = (TarotCardBuilder()
    .index(48).value(13).major_arcana(False).name("Queen of Cups")
    .upright("Compassion, Calm, and Comfort")
    .reversed("Martyrdom, Insecurity, and Dependence")
    .build())

define king_of_cups = (TarotCardBuilder()
    .index(49).value(14).major_arcana(False).name("King of Cups")
    .upright("Compassion, Control, and Balance")
    .reversed("Coldness, Moodiness, and Bad Advice")
    .build())

define ace_of_swords = (TarotCardBuilder()
    .index(50).value(1).major_arcana(False).name("Ace of Swords")
    .upright("Break Through, Clarity, and Sharp Mind")
    .reversed("Confusion, Brutality, and Chaos")
    .build())

define two_of_swords = (TarotCardBuilder()
    .index(51).value(2).major_arcana(False).name("2 of Swords")
    .upright("Difficult Choices, Indecision, and Stalemate")
    .reversed("Lesser of Two Evils, No Right Choice, and Confusion")
    .build())

define three_of_swords = (TarotCardBuilder()
    .index(52).value(3).major_arcana(False).name("3 of Swords")
    .upright("Heartbreak, Suffering, and Grief")
    .reversed("Recovery, Forgiveness, and Moving On")
    .build())

define four_of_swords = (TarotCardBuilder()
    .index(53).value(4).major_arcana(False).name("4 of Swords")
    .upright("Rest, Restoration, and Contemplation")
    .reversed("Restlessness, Burnout, and Stress")
    .build())

define five_of_swords = (TarotCardBuilder()
    .index(54).value(5).major_arcana(False).name("5 of Swords")
    .upright("Unbridled Ambition, Winning at All Cost, and Sneakiness")
    .reversed("Lingering Resentment, Desire to Reconcile, and Forgivness")
    .build())

define six_of_swords = (TarotCardBuilder()
    .index(55).value(6).major_arcana(False).name("6 of Swords")
    .upright("Transition, Leaving Behind, and Moving On")
    .reversed("Emotional Baggage, Unresolved Issues, and Resisting Transition")
    .build())

define seven_of_swords = (TarotCardBuilder()
    .index(56).value(7).major_arcana(False).name("7 of Swords")
    .upright("Deception, Trickery, as well as Tactics and Strategy")
    .reversed("Coming Clean, Rethinking Approach, and Deception")
    .build())

define eight_of_swords = (TarotCardBuilder()
    .index(57).value(8).major_arcana(False).name("8 of Swords")
    .upright("Imprisionment, Entrapment, and Self-Victimization")
    .reversed("Self-Acceptance, New Perspective, and Freedom")
    .build())

define nine_of_swords = (TarotCardBuilder()
    .index(58).value(9).major_arcana(False).name("9 of Swords")
    .upright("Anxiety, Hopelessness, and Trauma")
    .reversed("Hope, Reaching Out, and Despair")
    .build())

define ten_of_swords = (TarotCardBuilder()
    .index(59).value(10).major_arcana(False).name("10 of Swords")
    .upright("Failuer, Collapse, and Defeat")
    .reversed("Can't Get Worse, Only Upwards, and Inevitable End")
    .build())

define page_of_swords = (TarotCardBuilder()
    .index(60).value(11).major_arcana(False).name("Page of Swords")
    .upright("Curiosity, Restlessness, and Mental Energy")
    .reversed("Deception, Manipulation, and All Talk")
    .build())

define knight_of_swords = (TarotCardBuilder()
    .index(61).value(12).major_arcana(False).name("Knight of Swords")
    .upright("Action, Impulsiveness, and Defending Beliefs")
    .reversed("No Direction, Disregarding Consequences, and Unpredictability")
    .build())

define queen_of_swords = (TarotCardBuilder()
    .index(62).value(13).major_arcana(False).name("Queen of Swords")
    .upright("Complexity, Perceptivness, and Clear Mindedness")
    .reversed("Cold Hearted, Cruel, and Bitterness")
    .build())

define king_of_swords = (TarotCardBuilder()
    .index(63).value(14).major_arcana(False).name("King of Swords")
    .upright("Head over Heart, Discipline, and Truth")
    .reversed("Manipulative, Cruel, and Weakness")
    .build())

define ace_of_coins = (TarotCardBuilder()
    .index(64).value(1).major_arcana(False).name("Ace of Coins")
    .upright("Opportunity, Prosperity, and New Venture")
    .reversed("Lost Opportunity, Missed Chances, and Bad Investments")
    .build())

define two_of_coins = (TarotCardBuilder()
    .index(65).value(2).major_arcana(False).name("2 of Coins")
    .upright("Balanced Decisions, Priority, and Adapting to Change")
    .reversed("Loss of Balance, Disorganization, and Overwhelmed")
    .build())

define three_of_coins = (TarotCardBuilder()
    .index(66).value(3).major_arcana(False).name("3 of Coins")
    .upright("Teamwork, Collaboratin, and Building")
    .reversed("Lacking Teamwork, Disorganization, and Group Conflict")
    .build())

define four_of_coins = (TarotCardBuilder()
    .index(67).value(4).major_arcana(False).name("4 of Coins")
    .upright("Conservation, Frugality, and Security")
    .reversed("Greediness, Stinginess, and Possessiveness")
    .build())

define five_of_coins = (TarotCardBuilder()
    .index(68).value(5).major_arcana(False).name("5 of Coins")
    .upright("Need, Poverty, and Insecurity")
    .reversed("Recovery, Charity, and Improvement")
    .build())

define six_of_coins = (TarotCardBuilder()
    .index(69).value(6).major_arcana(False).name("6 of Coins")
    .upright("Charity, Generosity, and Sharing")
    .reversed("Strings Attached, Stinginess, Power and Domination")
    .build())

define seven_of_coins = (TarotCardBuilder()
    .index(70).value(7).major_arcana(False).name("7 of Coins")
    .upright("Hard Work, Perseverance, and Diligence")
    .reversed("Work Without Result, Distractions, and Lack of Reward")
    .build())

define eight_of_coins = (TarotCardBuilder()
    .index(71).value(8).major_arcana(False).name("8 of Coins")
    .upright("Apprenticeship, Passion, and High Standards")
    .reversed("Lack of Passion, Uninspired, and Lacking Motivation")
    .build())

define nine_of_coins = (TarotCardBuilder()
    .index(72).value(9).major_arcana(False).name("9 of Coins")
    .upright("Fruits of Labor, Rewards, and Luxury")
    .reversed("Reckless Spending, Living Beyond Means, and False Success")
    .build())

define ten_of_coins = (TarotCardBuilder()
    .index(73).value(10).major_arcana(False).name("10 of Coins")
    .upright("Legacy, Culmination, and Inheritance")
    .reversed("Fleeting Success, Lack of Stability, and Lack of Resources")
    .build())

define page_of_coins = (TarotCardBuilder()
    .index(74).value(11).major_arcana(False).name("Page of Coins")
    .upright("Ambition, Desire, and Diligence")
    .reversed("Lack of Commitment, Greediness, and Laziness")
    .build())

define knight_of_coins = (TarotCardBuilder()
    .index(75).value(12).major_arcana(False).name("Knight of Coins")
    .upright("Efficiency, Hard Work, and Responsibility")
    .reversed("Laziness, Obsessivness, and Work without Reward")
    .build())

define queen_of_coins = (TarotCardBuilder()
    .index(76).value(13).major_arcana(False).name("Queen of Coins")
    .upright("Practicallity, Creature Comforts, and Financial Security")
    .reversed("Self-Centeredness, Jealousy, and Smothering")
    .build())

define king_of_coins = (TarotCardBuilder()
    .index(77).value(14).major_arcana(False).name("King of Coins")
    .upright("Abundance, Prosperity, and Security")
    .reversed("Greed, Indulgence, and Sensuality")
    .build())