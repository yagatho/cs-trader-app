# All the functions that draw something in the terminal
import shutil
import config
import classes
import main
from rich.console import Console
from rich.markdown import Markdown
from InquirerPy import prompt
from InquirerPy.separator import Separator

# GLOBAL
console = Console(force_terminal=True, color_system="truecolor")

# MAIN FUNCTIONS


def draw_page(items: list, bot: str = "", top: str = "", msg: str = ""):
    """ Draws page with prompt made of items.
    Returns the answer. """
    clear_terminal()

    # Top line
    line_top = (shutil.get_terminal_size().columns -
                len(top) - 6) * "-"
    line_top += ' ' + top
    line_top += ' ----'
    print(line_top)

    # Bot line
    line_bot = (shutil.get_terminal_size().columns -
                len(bot) - 6) * "-"
    line_bot += ' ' + bot
    line_bot += ' ----'

    # Msg
    if msg == "":
        msg = "What do you want to do:"

    # Generate choice list
    items.insert(0, Separator("  "))
    question = [
        {
            "type": "list",
            "name": "menu",
                    "message": msg,
                    "choices": items,
            "long_instruction": line_bot,
        }
    ]

    # Get answer
    ans = prompt(question)
    return ans['menu']


def draw_menu_page(items: list, msg: str = ""):
    """ Draws menu page.
    Returns the index of the answer. """

    clear_terminal()

    line = shutil.get_terminal_size().columns * "-"

    # Draw header
    print(line + "\n CS Market Trader \n" + line)

    # Draw prompt
    items.insert(0, Separator(" "))
    if msg == "":
        msg = "What do you want to do:"

    question = [
        {
            "type": "list",
            "name": "menu",
                    "message": msg,
                    "choices": items,
        }
    ]

    ans = prompt(question)
    return items.index(ans['menu'])-1


def draw_item_page(item: classes.Item):
    """ Draws menu page.
    Returns back the market state. """

    clear_terminal()

    if item.float_val is not None:
        col = float_to_hex(item.float_val)

    mdf = "# " + str(item.name)
    mdf += "\n- `Offer ID:` " + str(item.id)
    mdf += "\n- `Offer type:` " + str(item.offer_type)
    mdf += "\n- `Vendor:` " + str(item.vendor)
    mdf += "\n- `Price:` " + str(item.price_latest) + " " + str(item.currency)
    mdf += "\n## Item Stats "
    mdf += "\n\n - `Item float:` " + \
        str(item.float_val) + " `" + item.wear + "`"
    mdf += "\n- `Item pattern:` " + str(item.paint_seed)
    mdf += "\n## Stickers "
    for i in item.stickers:
        mdf += f"\n- `Slot {i[0]}:` " + i[1:]

    console.print(Markdown(mdf))

    if item.float_val is not None:
        console.print(f"[{col}]███[/{col}]")

    # Wait
    input(" ")

    return main.ShowMarket()


# PAGE SPECIFIC FUNCTIONS
def draw_market_page(options: list, market: str = ""):
    """ Draw market page.
    Returns the index of the answer. """

    # Add the action buttons
    options.insert(0, "Search ")
    options.insert(1, Separator(" "))
    options.extend([Separator("\n\n"), "Next Page", "Prev Page", "Back"])

    # Create the bottom line and draw page
    bot_line = 'Page: ' + str(config.params.page)
    return draw_page(options, bot_line, market)


# HELPER FUNCTIONS
def clear_terminal():
    """  Just clear the terminal window """
    print("\033[H\033[J")


def float_to_hex(value):
    value = max(0, min(1, value))

    red = int(255 * value)
    green = int(255 * (1 - value))
    blue = 0

    hex_value = "#{:02x}{:02x}{:02x}".format(red, green, blue)

    return hex_value
