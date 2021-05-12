class STATICS():
    WOW_CLASSES_EMOJIS = [
        ':Warrior:839571089474322503',
        ':Rouge:839571089726504981',
        ':Hunter:839571088987521038',
        ':Warlock:839571089515610152',
        ':Shaman:839571089445355530',
        ':Druid:839571089427922964',
        ':Mage:839571089395154954',
        ':Paladin:839571089188323368',
        ':Priest:839571089171677224',
    ]


    SOLITAIRE_ROLES_MAP = {
        'Warrior': 'Krieger',
        'Rouge': 'Schurke',
        'Hunter': 'Jäger',
        'Warlock': 'Hexenmeister',
        'Shaman': 'Schamane',
        'Druid': 'Druide',
        'Mage': 'Magier',
        'Paladin': 'Paladin',
        'Priest': 'Priester'
    }

    MEMBER = 'Mitglied'
    GUEST = 'Gast'

    SOLITAIRE_ROLES = list(SOLITAIRE_ROLES_MAP.values())

    EMOJI_IDS = list(map(lambda x: str(x).split(':')[2], WOW_CLASSES_EMOJIS))
