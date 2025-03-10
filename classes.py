# File used to store all the helper classes

# Utils
from __future__ import annotations

class Params:
    """ Class used to store global query params across all the markets """

    def __init__(self, page: int, limit: int):
        self.page: int = page
        self.limit: int = limit


class State:
    """ State abstract construct for the state machine """

    def run(self) -> State | None:
        pass


class StateMachine:
    """ State machine main """

    def __init__(self, baseState: State):
        self.state: State = baseState

    def run(self):
        return self.state.run()

    def change_state(self, state: State):
        self.state = state


class Item:
    def __init__(self):

        self.id:int | None = None
        self.name:str | None = None
        self.price:float | None = None
        self.vendor:str | None = None
        self.offer_type:str | None = None
        self.header:str | None = None
        self.float_val:float | None = None
        self.paint_seed:int | None = None
        self.currency:str | None = None
        self.wear:str | None = "(BS)"
        self.stickers:list[str] | None = []


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
