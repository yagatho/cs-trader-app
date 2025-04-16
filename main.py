# Main program file
import config

# Util
from modules.classes import State
from modules.classes import StateMachine

# Graphics
from modules.graphics import draw_menu_page
from modules.graphics import draw_market_page
from modules.graphics import clear_terminal

import modules.itemParsers as itemParsers
from rich.console import Console
from InquirerPy.separator import Separator
from typing_extensions import override

# Console instance
console = Console()


# STATES
# Main menu state
class MainMenu(State):
    @override
    def run(self):
        ans = draw_menu_page(['Go to market', 'Quit'])

        if ans == 0:
            return ShowMarket()
        else:
            return None


# Market selection state
class MarketSelect(State):
    @override
    def run(self):
        config.curr_market = draw_menu_page(
            ['Cs Float', 'Steam', Separator(" "), "Back"],
            "What market you want to search?"
        )

        return ShowMarket()


# Market offers state
class ShowMarket(State):
    @override
    def run(self):
        options: list[str | Separator] = []

        # Visual indicator of getting item data
        curr_parser = itemParsers.csfloat
        with console.status(f"[bold green]Getting {curr_parser.name} item data..."):
            # Get all items
            options += curr_parser.get_item_list()

        # itemParsers.steam.get_steam_price()
        ans = draw_market_page(options, curr_parser.name)

        # Return next state
        return config.change_market_page(ans)


# MAIN PROGRAM LOOP
if (__name__ == "__main__"):
    # Init statemachine
    sm = StateMachine(MainMenu())

    while True:
        ans = sm.run()

        # End program if answer in None
        if ans is not None:
            sm.change_state(ans)
        else:
            clear_terminal()
            break
