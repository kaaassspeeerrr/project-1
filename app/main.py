import tweepy

from authorization_tokens import *

# import random
random_number = 3

if random_number == 0:
        #option1
        #Pick a phrase randomly from a list of phrases:
        phrase_list = ["Hi my name is Kasper",
                        "Kasper is my name",
                        "I like Twitter Bots"]
        random_number = random.randrange( len(phrase_list))
        message = phrase_list[random_number]
elif random_number == 1:
        #option 2
        # Create a sentence template with some blanks, and
        #randomly pick a word from a list to fill in each blank.
        word_list = ["apples", "bananas", "carrots", "dates"]

        string_template = "Some people think {} are good, but I like {}."

        random_number = random.randrange( len(word_list))
        word1 = word_list[random_number]

        random_number = random.randrange( len(word_list))
        word2 = word_list[random_number]

        message = string_template.format(word1, word2)
elif random_number == 2:
        #option 3
        #Randomly pick a template from a list, then randomly pick word_list
        #from a word list, and use the words to fill in the string_template

        word_list = ["people", "video games", "sports", "people"]
        template_list = ["If you like {}, you'll love {}.",
                        "You might think I'm a {} person, but actually I love {}.",
                        "You'd never guess it, but I like {} even more than {}."]

        random_number = random.randrange( len(template_list))
        template = template_list[random_number]

        random_number = random.randrange( len(word_list))
        word1 = word_list[random_number]

        random_number = random.randrange( len(word_list))
        word2 = word_list[random_number]

        message = template.format(word1, word2)
elif random_number == 3:
    # Kasper Bielecki 09/12/2020
    # Dungeons and Dragans Charachter Generator
    # Based on a Java Program I worked on between the dates of 04/17/2019 - 09/12/2020
    #*************CHECKLIST*************
    #
    # - Physical Attributes -
    # [*] Race
    # [*] Sub Race
    # [*] Sex
    # [*] Height
    # [*] Weight
    # [*] Age and agebracket
    # [] Eyes
    # [] Skin
    # [] Hair
    #
    # - Character Traits -
    # [*] Alignment
    # [*] Class
    # [] Background
    # [] Proficiencies
    # [] Character Name
    # [] Skills
    # [] Languages
    # [] Personality Traits
    # [] Ideals
    # [] Bonds
    # [] Flaws
    #
    # - Statistics -
    # [] Level
    # [*] Abilities
    # [*] Modifiers
    # [] Saving Throws
    # [] Hit Points
    # [] Hit Dice
    # [] Perception
    # [] Spell Casting Ability
    # [] Spell Save DC
    # [] Spell Attack Bonus
    # [] Spell Casting Class
    #
    # - Others -
    # [] Attacks
    # [] Equipment
    # [] Spells
    #
    #*******************************
    import random

    #04 Sided Die
    def D4():
    	x = (random.randrange(1,5))
    	return x

    #06 Sided Die
    def D6():
    	x = (random.randrange(1,7))
    	return x

    #08 Sided Die
    def D8():
    	x = (random.randrange(1,9))
    	return x

    #10 Sided Die
    def D10():
    	x = (random.randrange(1,11))
    	return x

    #Ability Score Roll
    def ability_score_roll():
        roll1 = D6()
        roll2 = D6()
        roll3 = D6()
        roll4 = D6()

        rolls = [
        roll1,
        roll2,
        roll3,
        roll4
        ]

        rolls.sort()

        ability_score = rolls[1] + rolls[2] + rolls[3]
        return ability_score

    def modifier_(ability):
        if ability == 1:
            return "(-5)"
        elif ability == 2 or ability == 3:
            return "(-4)"
        elif ability == 4 or ability == 5:
            return "(-3)"
        elif ability == 6 or ability == 7:
            return "(-2)"
        elif ability == 8 or ability == 9:
            return "(-1)"
        elif ability == 10 or ability == 11:
            return "(+0)"
        elif ability == 12 or ability == 13:
            return "(+1)"
        elif ability == 14 or ability == 15:
            return "(+2)"
        elif ability == 16 or ability == 17:
            return "(+3)"
        elif ability == 18 or ability == 19:
            return "(+4)"
        elif ability == 20 or ability == 21:
            return "(+5)"
        elif ability == 22 or ability == 23:
            return "(+6)"
        elif ability == 24 or ability == 25:
            return "(+7)"
        elif abilit == 26 or ability == 27:
            return "(+8)"
        elif ability == 28 or ability == 29:
            return "(+9)"
        elif ability == 30:
             return "(+10)"

    #Race
    race_list = [
    "Dragonborn",
    "Dwarf",
    "Elf",
    "Gnome",
    "Half-Elf",
    "Halfling",
    "Half-Orc",
    "Human",
    "Tiefling"
    ]
    random_number = random.randrange( len(race_list))
    race = race_list[random_number]

    #Sub Race
    if race == "Dwarf":
        subrace_list = [
        "Hill",
        "Mountain"
        ]
        random_number = random.randrange( len(subrace_list))
        subrace = subrace_list[random_number]

    elif race == "Elf":
        subrace_list = [
        "High",
        "Wood",
        "Drow"
        ]
        random_number = random.randrange( len(subrace_list))
        subrace = subrace_list[random_number]

    elif race == "Halfling":
        subrace_list = [
        "Lightfoot",
        "Stout"
        ]
        random_number = random.randrange( len(subrace_list))
        subrace = subrace_list[random_number]

    elif race == "Human":
        subrace_list = [
        "Calishite",
        "Chondathan",
        "Damaran",
        "Illuskan",
        "Mulan",
        "Rashemi",
        "Shou",
        "Tethyrian",
        "Turami"
        ]
        random_number = random.randrange( len(subrace_list))
        subrace = subrace_list[random_number]

    elif race == "Dragonborn":
        subrace_list = [
        "Black",
        "Blue",
        "Brass",
        "Bronze",
        "Copper",
        "Gold",
        "Green",
        "Red",
        "Silver",
        "White"
        ]
        random_number = random.randrange( len(subrace_list))
        subrace = subrace_list[random_number]

    elif race == "Gnome":
        subrace_list = [
        "Forrest",
        "Rock"
        ]
        random_number = random.randrange( len(subrace_list))
        subrace = subrace_list[random_number]

    else:
        subrace = None

    #Class
    class_list = [
    "Barbarian",
    "Bard",
    "Cleric",
    "Druid",
    "Fighter",
    "Monk",
    "Paladin",
    "Ranger",
    "Rogue"
    ]
    random_number = random.randrange( len(class_list))
    class_ = class_list[random_number]

    #Sex
    sex_list = [
    "Male",
    "Female"
    ]
    random_number = random.randrange( len(sex_list))
    sex = sex_list[random_number]

    #Height and Weight
    if race == "Dragonborn":
        roll = D8() + D8()
        feet = int((66 + roll) / 12)
        inches = (66 + roll) % 12
        weight = ((roll * (D6()+D6())) + 175)

    elif race == "Dwarf":
        if subrace == "Hill":
            roll = D4() + D4()
            feet = int((44 + roll) / 12)
            inches = (44 + roll) % 12
            weight = ((roll * (D6()+D6())) + 115)

        elif subrace == "Mountain":
            roll = D4() + D4()
            feet = int((48 + roll) / 12)
            inches = (48 + roll) % 12
            weight = ((roll * (D6()+D6())) + 130)

    elif race == "Elf":
        if subrace == "High":
            roll = D10() + D10()
            feet = int((54 + roll) / 12)
            inches = (54 + roll) % 12
            weight = ((roll * D4()) + 90)

        elif subrace == "Wood":
            roll = D10() + D10()
            feet = int((54 + roll) / 12)
            inches = (54 + roll) % 12
            weight = ((roll * D4()) + 100)

        elif subrace == "Drow":
            roll = D6() + D6()
            feet = int((53 + roll) / 12)
            inches = (53 + roll) % 12
            weight = ((roll * D6()) + 75)

    elif race == "Gnome":
        roll = D4() + D4()
        feet = int((35 + roll) / 12)
        inches = (35 + roll) % 12
        weight = ((roll * 1) + 35)

    elif race == "Half-Elf":
        roll = D8() + D8()
        feet = int((57 + roll) / 12)
        inches = (57 + roll) % 12
        weight = ((roll * (D4()+D4())) + 110)

    elif race == "Halfling":
        roll = D4() + D4()
        feet = int((31 + roll) / 12)
        inches = (31 + roll) % 12
        weight = ((roll * 1) + 35)

    elif race == "Half-Orc":
        roll = D10() + D10()
        feet = int((58 + roll) / 12)
        inches = (58 + roll) % 12
        weight = ((roll * (D6()+D6())) + 140)

    elif race == "Human":
        roll = D10() + D10()
        feet = int((56 + roll) / 12)
        inches = (56 + roll) % 12
        weight = ((roll * (D4()+D4())) + 110)

    elif race == "Tiefling":
        roll = D8() + D8()
        feet = int((57 + roll) / 12)
        inches = (57 + roll) % 12
        weight = ((roll * (D4()+D4())) + 110)

    height_template = '''{}'{}"'''
    height, weight = (height_template.format(feet, inches), weight)

    #Age and Age Bracket
    if race == "Human":
        age = (random.randrange(6,91))
        if age < 18:
            age_bracket = "years old - Childhood"
        elif age >= 18 and age < 30:
            age_bracket = "years old - Young Adult"
        elif age >= 30 and age < 65:
            age_bracket = "years old - Settled Adult"
        elif age >= 65 and age <= 90:
            age_bracket = "years old - Elderly"

    elif race == "Dwarf":
        age = (random.randrange(6,351))
        if age < 18:
            age_bracket = "years old - Childhood"
        elif age >= 18 and age < 50:
            age_bracket = "years old - Young Adult"
        elif age >= 50 and age < 200:
            age_bracket = "years old - Settled Adult"
        elif age >= 200 and age <= 350:
            age_bracket = "years old - Elderly"

    elif race == "Elf":
        age = (random.randrange(6,751))
        if age < 100:
            age_bracket = "years old - Childhood"
        elif age >= 100 and age < 450:
            age_bracket = "years old - Young Adult"
        elif age >= 450 and age < 650:
            age_bracket = "years old - Settled Adult"
        elif age >= 650 and age <= 750:
            age_bracket = "years old - Elderly"

    elif race == "Halfling":
        age = (random.randrange(6,251))
        if age < 20:
            age_bracket = "years old - Childhood"
        elif age >= 20 and age < 40:
            age_bracket = "years old - Young Adult"
        elif age >= 40 and age < 150:
            age_bracket = "years old - Settled Adult"
        elif age >= 150 and age <= 250:
            age_bracket = "years old - Elderly"

    elif race == "Dragonborn":
        age = (random.randrange(1,81))
        if age < 15:
            age_bracket = "years old - Childhood"
        elif age >= 15 and age < 20:
            age_bracket = "years old - Young Adult"
        elif age >= 20 and age < 50:
            age_bracket = "years old - Settled Adult"
        elif age >= 50 and age <= 80:
            age_bracket = "years old - Elderly"

    elif race == "Gnome":
        age = (random.randrange(6,401))
        if age < 20:
            age_bracket = "years old - Childhood"
        elif age >= 20 and age < 40:
            age_bracket = "years old - Young Adult"
        elif age >= 40 and age < 200:
            age_bracket = "years old - Settled Adult"
        elif age >= 200 and age <= 400:
            age_bracket = "years old - Elderly"

    elif race == "Half-Elf":
        age = (random.randrange(6,181))
        if age < 20:
            age_bracket = "years old - Childhood"
        elif age >= 20 and age < 50:
            age_bracket = "years old - Young Adult"
        elif age >= 50 and age < 150:
            age_bracket = "years old - Settled Adult"
        elif age >= 150 and age <= 180:
            age_bracket = "years old - Elderly"

    elif race == "Half-Orc":
        age = (random.randrange(1,76))
        if age < 14:
            age_bracket = "years old - Childhood"
        elif age >= 14 and age < 45:
            age_bracket = "years old - Young Adult"
        elif age >= 45 and age < 60:
            age_bracket = "years old - Settled Adult"
        elif age >= 60 and age <= 75:
            age_bracket = "years old - Elderly"

    elif race == "Tiefling":
        age = (random.randrange(6,101))
        if age < 18:
            age_bracket = "years old - Childhood"
        elif age >= 18 and age < 40:
            age_bracket = "years old - Young Adult"
        elif age >= 40 and age < 70:
            age_bracket = "years old - Settled Adult"
        elif age >= 70 and age <= 100:
            age_bracket = "years old - Elderly"

    #Alignment
    alignment_list = [
    "Lawful Good",
    "Neutral Good",
    "Chaotic Good",
    "Lawful Neutral",
    "True Neutral",
    "Chaotic Neutral",
    "Lawful Evil",
    "Neutral Evil",
    "Chaotic Evil"
    ]
    random_number = random.randrange( len(alignment_list))
    alignment = alignment_list[random_number]

    #Abilities
    ability1 = ability_score_roll()
    ability2 = ability_score_roll()
    ability3 = ability_score_roll()
    ability4 = ability_score_roll()
    ability5 = ability_score_roll()
    ability6 = ability_score_roll()

    abilities = [ability1,ability2,ability3,ability4,ability5,ability6]
    abilities.sort()

    if class_ == "Barbarian":
        strength = abilities[4]
        dexterity = abilities[3]
        constitution = abilities[5]
        intelligence = abilities[0]
        wisdom = abilities[1]
        charisma = abilities[2]
    elif class_ == "Bard":
        strength = abilities[1]
        dexterity = abilities[4]
        constitution = abilities[3]
        intelligence = abilities[0]
        wisdom = abilities[2]
        charisma = abilities[5]
    elif class_ == "Cleric":
        strength = abilities[4]
        dexterity = abilities[1]
        constitution = abilities[3]
        intelligence = abilities[0]
        wisdom = abilities[5]
        charisma = abilities[2]
    elif class_ == "Druid":
        strength = abilities[0]
        dexterity = abilities[4]
        constitution = abilities[3]
        intelligence = abilities[1]
        wisdom = abilities[5]
        charisma = abilities[2]
    elif class_ == "Fighter":
        strength = abilities[5]
        dexterity = abilities[3]
        constitution = abilities[4]
        intelligence = abilities[0]
        wisdom = abilities[1]
        charisma = abilities[2]
    elif class_ == "Monk":
        strength = abilities[0]
        dexterity = abilities[5]
        constitution = abilities[3]
        intelligence = abilities[1]
        wisdom = abilities[4]
        charisma = abilities[2]
    elif class_ == "Paladin":
        strength = abilities[5]
        dexterity = abilities[2]
        constitution = abilities[4]
        intelligence = abilities[0]
        wisdom = abilities[1]
        charisma = abilities[3]
    elif class_ == "Ranger":
        strength = abilities[0]
        dexterity = abilities[5]
        constitution = abilities[3]
        intelligence = abilities[1]
        wisdom = abilities[4]
        charisma = abilities[2]
    elif class_ == "Rogue":
        strength = abilities[3]
        dexterity = abilities[5]
        constitution = abilities[2]
        intelligence = abilities[0]
        wisdom = abilities[1]
        charisma = abilities[4]
    elif class_ == "Sorcerer":
        strength = abilities[0]
        dexterity = abilities[4]
        constitution = abilities[3]
        intelligence = abilities[1]
        wisdom = abilities[2]
        charisma = abilities[5]
    elif class_ == "Warlock":
        strength = abilities[1]
        dexterity = abilities[3]
        constitution = abilities[4]
        intelligence = abilities[0]
        wisdom = abilities[2]
        charisma = abilities[5]
    elif class_ == "Wizard":
        strength = abilities[0]
        dexterity = abilities[3]
        constitution = abilities[4]
        intelligence = abilities[5]
        wisdom = abilities[2]
        charisma = abilities[1]

    if race == "Dwarf":
        constitution = constitution + 2
        if subrace == "Hill":
            wisdom = wisdom + 1
        elif subrace == "Mountain":
            strength = strength + 2
    elif race == "Elf":
        dexterity = dexterity + 2
        if subrace == "High":
            intelligence = intelligence + 1
        elif subrace == "Drow":
            charisma = charisma + 1
        elif subrace == "Wood":
            wisdow = wisdom + 1
    elif race == "Halfling":
        dexterity = dexterity + 2
        if subrace == "Lightfoot":
            charisma = charisma + 1
        elif subrace == "Stout":
            constitution = constitution + 1
    elif race == "Human":
        strength = strength + 1
        dexterity = dexterity + 1
        constitution = constitution + 1
        intelligence = intelligence + 1
        wisdom = wisdom + 1
        charisma = charisma + 1
    elif race == "Dragonborn":
        strength = strength + 2
        charisma = charisma + 1
    elif race == "Gnome":
        intelligence = intelligence + 2
        if subrace == "Forrest":
            dexterity = dexterity + 1
        elif subrace == "Rock":
            constitution = constitution + 1
    elif race == "Half-Elf":
        charisma = charisma + 2
        abilitiy_choices = ["strength","dexterity","constitution","intelligence","wisdom","charisma"]
        random_number = random.randrange( len(abilitiy_choices))
        if abilitiy_choices[random_number] == "strength":
            strength = strength +1
            abilities.pop(0)
            random_number = random.randrange( len(abilitiy_choices))
            if abilitiy_choices[random_number] == "dexterity":
                dexterity = dexterity + 1
            elif abilitiy_choices[random_number] == "constitution":
                constitution = constitution + 1
            elif abilitiy_choices[random_number] == "intelligence":
                intelligence = intelligence + 1
            elif abilitiy_choices[random_number] == "wisdom":
                wisdom = wisdom + 1
            elif abilitiy_choices[random_number] == "charisma":
                charisma = charisma + 1
        elif abilitiy_choices[random_number] == "dexterity":
            dexterity = dexterity +1
            abilities.pop(1)
            random_number = random.randrange( len(abilitiy_choices))
            if abilitiy_choices[random_number] == "strength":
                strength = strength + 1
            elif abilitiy_choices[random_number] == "constitution":
                constitution = constitution + 1
            elif abilitiy_choices[random_number] == "intelligence":
                intelligence = intelligence + 1
            elif abilitiy_choices[random_number] == "wisdom":
                wisdom = wisdom + 1
            elif abilitiy_choices[random_number] == "charisma":
                charisma = charisma + 1
        elif abilitiy_choices[random_number] == "constitution":
            constitution = constitution +1
            abilities.pop(2)
            random_number = random.randrange( len(abilitiy_choices))
            if abilitiy_choices[random_number] == "strength":
                strength = strength + 1
            elif abilitiy_choices[random_number] == "dexterity":
                dexterity = dexterity + 1
            elif abilitiy_choices[random_number] == "intelligence":
                intelligence = intelligence + 1
            elif abilitiy_choices[random_number] == "wisdom":
                wisdom = wisdom + 1
            elif abilitiy_choices[random_number] == "charisma":
                charisma = charisma + 1
        elif abilitiy_choices[random_number] == "intelligence":
            intelligence = intelligence +1
            abilities.pop(3)
            random_number = random.randrange( len(abilitiy_choices))
            if abilitiy_choices[random_number] == "strength":
                strength = strength + 1
            elif abilitiy_choices[random_number] == "dexterity":
                dexterity = dexterity + 1
            elif abilitiy_choices[random_number] == "constitution":
                constitution = constitution + 1
            elif abilitiy_choices[random_number] == "wisdom":
                wisdom = wisdom + 1
            elif abilitiy_choices[random_number] == "charisma":
                charisma = charisma + 1
        elif abilitiy_choices[random_number] == "wisdom":
            wisdom = wisdom +1
            abilities.pop(4)
            random_number = random.randrange( len(abilitiy_choices))
            if abilitiy_choices[random_number] == "strength":
                strength = strength + 1
            elif abilitiy_choices[random_number] == "dexterity":
                dexterity = dexterity + 1
            elif abilitiy_choices[random_number] == "constitution":
                constitution = constitution + 1
            elif abilitiy_choices[random_number] == "intelligence":
                intelligence = intelligence + 1
            elif abilitiy_choices[random_number] == "charisma":
                charisma = charisma + 1
        elif abilitiy_choices[random_number] == "charisma":
            charisma = charisma +1
            abilities.pop(5)
            random_number = random.randrange( len(abilitiy_choices))
            if abilitiy_choices[random_number] == "strength":
                strength = strength + 1
            elif abilitiy_choices[random_number] == "dexterity":
                dexterity = dexterity + 1
            elif abilitiy_choices[random_number] == "constitution":
                constitution = constitution + 1
            elif abilitiy_choices[random_number] == "intelligence":
                intelligence = intelligence + 1
            elif abilitiy_choices[random_number] == "wisdom":
                wisdom = wisdom + 1
    elif race == "Half-Orc":
        strength = strength + 2
        constitution = constitution + 1
    elif race == "Tiefling":
        intelligence = intelligence +1
        charisma = charisma + 2

    strength_modifier = modifier_(strength)
    dexterity_modifier = modifier_(dexterity)
    constitution_modifier = modifier_(constitution)
    intelligence_modifier = modifier_(intelligence)
    wisdom_modifier = modifier_(wisdom)
    charisma_modifier = modifier_(charisma)
    #Print
    if subrace == None:
        # print("Race:",race,
        # "\nClass:",class_,
        # "\nAlignment:",alignment,
        # "\nSex:",sex,
        # "\nHeight:",height,
    	# "\nWeight:",weight,"lbs",
        # "\nAge:",age,age_bracket,
        # "\nStrength:",strength,strength_modifier,
        # "\nDexterity:",dexterity,dexterity_modifier,
        # "\nConstitution:",constitution,constitution_modifier,
        # "\nIntelligence:",intelligence,intelligence_modifier,
        # "\nWisdom:",wisdom,wisdom_modifier,
        # "\nCharisma:",charisma,charisma_modifier,)

        template = "Race: {}\nClass: {}\nAlignment: {}\nSex: {}\nHeight: {}\nWeight: {} Lbs\nAge: {} {}\nStrength: {} {}\nDexterity: {} {}\nConstitution {} {}\nIntelligence: {} {}\nWisdom: {} {}\nCharisma {} {}"
        message = template.format(race,class_,alignment,sex,height,weight,age,age_bracket,strength,strength_modifier,dexterity,dexterity_modifier,constitution,constitution_modifier,intelligence,intelligence_modifier,wisdom,wisdom_modifier,charisma,charisma_modifier)
    else:
        # print("Race:",subrace,race,
        # "\nClass:",class_,
        # "\nAlignment:",alignment,
        # "\nSex:",sex,
        # "\nHeight:",height,
    	# "\nWeight:",weight,"lbs",
        # "\nAge:",age,age_bracket,
        # "\nStrength:",strength,strength_modifier,
        # "\nDexterity:",dexterity,dexterity_modifier,
        # "\nConstitution:",constitution,constitution_modifier,
        # "\nIntelligence:",intelligence,intelligence_modifier,
        # "\nWisdom:",wisdom,wisdom_modifier,
        # "\nCharisma:",charisma,charisma_modifier,)
        template = "Race: {} {}\nClass: {}\nAlignment: {}\nSex: {}\nHeight: {}\nWeight: {} Lbs\nAge: {} {}\nStrength: {} {}\nDexterity: {} {}\nConstitution {} {}\nIntelligence: {} {}\nWisdom: {} {}\nCharisma {} {}"
        message = template.format(subrace,race,class_,alignment,sex,height,weight,age,age_bracket,strength,strength_modifier,dexterity,dexterity_modifier,constitution,constitution_modifier,intelligence,intelligence_modifier,wisdom,wisdom_modifier,charisma,charisma_modifier)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status(message)
print("Done.")