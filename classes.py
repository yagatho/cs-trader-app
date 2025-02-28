# File used to store all the helper classes


class Params:
    """ Class used to store global query params across all the markets """

    def __init__(self, page, limit):
        self.page = page
        self.limit = limit


class State:
    """ State abstract construct for the state machine """

    def run(self):
        pass


class StateMachine:
    """ State machine main """

    def __init__(self, baseState: State):
        self.state = baseState

    def run(self):
        return self.state.run()

    def change_state(self, state: State):
        self.state = state


class Item:
    def __init__(self, id: str = "", name: str = "", pricelat: float = 0,
                 pricesold: float = 0, vendor: str = "", offer_type: str = "",
                 header: str = "", float_val: float = 0, paint_seed: int = 0,
                 currency: str = ""
                 ):

        self.id = id
        self.name = name
        self.price_latest = pricelat
        self.price_sold = pricesold
        self.vendor = vendor
        self.offer_type = offer_type
        self.header = header
        self.float_val = float_val
        self.paint_seed = paint_seed
        self.currency = currency
        self.wear = "(BS)"
        self.stickers = []

    def check_float(self):
        if self.float_val is None:
            self.wear = ""
            return

        if self.float_val > 0.44:
            self.wear = "(BS)"
        elif self.float_val > 0.37 and self.float_val < 0.44:
            self.wear = "(WW)"
        elif self.float_val > 0.15 and self.float_val < 0.37:
            self.wear = "(FT)"
        elif self.float_val > 0.07 and self.float_val < 0.15:
            self.wear = "(MW)"
        elif self.float_val < 0.07:
            self.wear = "(FN)"
