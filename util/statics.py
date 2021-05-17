class STATICS():
    WOW_CLASSES_EMOJIS = [
        ':Warrior:843898101148549190',
        ':Rouge:843898101420654623',
        ':Hunter:843897480047099934',
        ':Warlock:843898101117747221',
        ':Shaman:843898101458272256',
        ':Druid:843897169349705761',
        ':Mage:843898101097693247',
        ':Paladin:843898101348958229',
        ':Priest:843898105685737505',
    ]


    SOLITAIRE_ROLES_MAP = {
        'Warrior': 'Krieger',
        'Rogue': 'Schurke',
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
