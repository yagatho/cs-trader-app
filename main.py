# Main program file
import config
import graphics
import classes
import itemParsers
from rich.console import Console
from InquirerPy.separator import Separator

# Console instance
console = Console()


# STATES
# Main menu state
class MainMenu(classes.State):
    def run(self):
        ans = graphics.draw_menu_page(['Go to market', 'Quit'])

        if ans == 0:
            return ShowMarket()
        else:
            return None


# Market selection state
class MarketSelect(classes.State):
    def run(self):
        config.curr_market = graphics.draw_menu_page(
            ['Cs Float', 'Steam', Separator(" "), "Back"],
            "What market you want to search?"
        )

        return ShowMarket()


# Market offers state
class ShowMarket(classes.State):
    def run(self):
        options = []
        for itemP in itemParsers.parsers:
            # Visual indicator of getting item data
            with console.status(f"[bold green]Getting {itemP.name} item data..."):
                # Get all items
                options += itemP.get_item_list()

        itemParsers.steam.get_steam_price()
        ans = graphics.draw_market_page(options, itemP.name)

        # Return next state
        return config.change_market_page(ans)


# MAIN PROGRAM LOOP
if (__name__ == "__main__"):
    # Init statemachine
    sm = classes.StateMachine(MainMenu())

    while True:
        ans = sm.run()

        # End program if answer in None
        if ans is not None:
            sm.change_state(ans)
        else:
            graphics.clear_terminal()
            break
