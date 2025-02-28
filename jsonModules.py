# All the API communication basic functions

import network
import config


def get_json_csfloat():
    """ Main functions for the csfloat market API communication """
    apiKey = "rOXCbHiNIPc6X5mhO_FPjFR5iBx5jPhh"
    errorDictionary = {
        400: "Bad Request -- Your request is invalid.",
        401: "Unauthorized -- Your API key is wrong.",
        403: "Forbidden -- The kitten requested is hidden for administrators only.",
        404: "Not Found -- The specified kitten could not be found.",
        405: "Method Not Allowed -- You tried to access a kitten with an invalid method.",
        406: "Not Acceptable -- You requested a format that isn't json.",
        410: "Gone -- The kitten requested has been removed from our servers.",
        418: "I'm a teapot.",
        429: "Too Many Requests -- You're requesting too many kittens! Slow down!",
        500: "Internal Server Error -- We had a problem with our server. Try again later.",
        503: "Service Unavailable -- We're temporarily offline for maintenance. Please try again later.,"
    }

    query = {
        "page": config.params.page,
        "limit": config.params.limit,
        "category": 0
    }

    if config.market_name:
        query["market_hash_name"] = config.market_name

    headers = {
        "authorization": apiKey,
        "content-type": "application/json"
    }

    return network.get_json(
        'https://csfloat.com/api/v1/listings', errorDictionary, query, headers
    )


def get_json_steam():
    """ Main functions for the steam market API communication """
    apiKey = "G6QTLV3LOIZJ8OJ0"
    errorDictionary = {
        400: "Bad Request -- Your request is invalid.",
        401: "Unauthorized -- Your API key is wrong.",
        403: "Forbidden -- The kitten requested is hidden for administrators only.",
        404: "Not Found -- The specified kitten could not be found.",
        405: "Method Not Allowed -- You tried to access a kitten with an invalid method.",
        406: "Not Acceptable -- You requested a format that isn't json.",
        410: "Gone -- The kitten requested has been removed from our servers.",
        418: "I'm a teapot.",
        429: "Too Many Requests -- You're requesting too many kittens! Slow down!",
        500: "Internal Server Error -- We had a problem with our server. Try again later.",
        503: "Service Unavailable -- We're temporarily offline for maintenance. Please try again later.,"
    }

    query = {
        "key": apiKey,
        "page": config.params.page,
        "max": config.params.limit,
    }

    if config.market_name != "":
        query["item_type"] = config.curr_item
        query["item_name"] = config.curr_skin

    headers = {
    }

    return network.get_json(
        'https://www.steamwebapi.com/steam/api/items', errorDictionary, query, headers
    )


def get_json_skinport():
    """ Main functions for the skinport market API communication """
    apiKey = "wEXH/XQBe/zL9S0hu8yfVYhmDkWMYLim3F8eE4Us13ctAuIcnL1DJT8jh3dAPvKKhD+DwhCEnzEyB6KtSHeKOg=="
