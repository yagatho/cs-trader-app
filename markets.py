# Used to store the states for each seperate markets at least for now

import classes
import config
import utility
import json
import main
from InquirerPy import prompt


# Search engine
class Search(classes.State):
    def run(self):
        with open("data.json", "r") as file:
            jsonf = json.load(file)

        dict = {item: None for item in list(jsonf.keys())}

        questions = [
            {
                "type": "input",
                "message": "What item?:",
                "completer": dict,
                "multicolumn_complete": True,
            },
        ]

        config.curr_item = prompt(questions)[0]

        config.curr_wear = utility.long_rawlist(config.wear)

        config.market_name = config.curr_item + " " + config.curr_wear
        return main.ShowMarket()
