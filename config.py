# File used to store all the global variables that are not for temp debug

from modules.classes import Item
from modules.classes import Params

import main

# Global var
params = Params(1, 25)
curr_market = 0
item_list = []

market_name = ""
curr_wear = ""
curr_skin = ""
curr_item = ""

pistols = [
    "Glock-18",
    "P2000",
    "USP-S",
    "Dual Berettas",
    "P250",
    "Tec-9",
    "Five-SeveN",
    "CZ75-Auto",
    "Desert Eagle",
    "R8 Revolver"
]

rifles = [
    "Galil AR",
    "FAMAS",
    "AK-47",
    "M4A4",
    "M4A1-S",
    "SSG 08",
    "SG 553",
    "AUG",
    "AWP",
    "G3SG1",
    "SCAR-20"
]

shotguns = [
    "Nova",
    "XM1014",
    "Sawed-Off",
    "MAG-7"
]

smgs = [
    "MAC-10",
    "MP9",
    "MP7",
    "MP5-SD",
    "UMP-45",
    "P90",
    "PP-Bizon"
]

heavy = [
    "M249",
    "Negev"
]

melee = [
    "Bayonet",
    "Butterfly Knife",
    "Karambit",
    "M9 Bayonet",
    "Huntsman Knife",
    "Shadow Daggers",
    "Bowie Knife",
    "Falchion Knife",
    "Gut Knife",
    "Flip Knife",
    "Stiletto Knife",
    "Ursus Knife",
    "Navaja Knife",
    "Nomad Knife",
    "Skeleton Knife",
    "Paracord Knife",
    "Survival Knife",
    "Classic Knife"
]

all_weapons = pistols + rifles + shotguns + smgs + heavy

skins = {
    "Glock-18": [
        "Fade",
        "Gamma Doppler",
        "Synth Leaf",
        "Twilight Galaxy",
        "Franklin",
        "Sand Dune",
        "Groundwater",
        "Red Tire",
        "Death Rattle",
        "Reactor",
        "Steel Disruption",
        "Night",
        "Brass",
        "Grinder",
        "Wraiths",
        "Warhawk",
        "Sacrifice",
        "Blue Fissure",
        "Oxide Blaze",
        "High Beam",
        "Ironwork",
        "Catacombs",
        "Royal Legion",
        "Pink DDPAT",
        "Off World",
        "Bunsen Burner",
        "Winterized",
        "Clear Polymer",
        "Weasel",
        "Snack Attack",
        "Dragon Tattoo",
        "Ramse's Reach",
        "Nuclear Garden",
        "Candy Apple",
        "Wasteland Rebel",
        "Teal Graf",
        "Moonrise",
        "Umbral Rabbit",
        "Neo-Noir",
        "Bullet Queen",
        "Block-18",
        "Water Elemental",
        "AXIA",
        "Vogue",
        "Gold Toof"
    ]
}

wear = [
    "(Factory New)",
    "(Minimal Wear)",
    "(Field-Tested)",
    "(Well-Worn)",
    "(Battle-Scarred)",
]


def change_market_page(ans: str):
    """ Change the global page var and return right state """
    global params

    if ans == "Back":
        return main.MainMenu()

    elif ans == "Prev Page":
        if params.page > 1:
            params.page -= 1

        return main.ShowMarket()

    elif ans == "Next Page":
        params.page += 1
        return main.ShowMarket()
    elif ans == "Search ":
        return markets.Search()
    else:
        global item_list
        result: list[Item] = list(
            filter(lambda item: item.header ==
                   ans, item_list)
        )

        return graphics.draw_item_page(result[0])
