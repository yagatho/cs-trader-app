import jsonModules
import classes
import config
import shutil
import requests
from bs4 import BeautifulSoup


class item_parser():
    """ Abstract construct made to get normalized item data from different endpoints """

    def __init__(self, name):
        self.name = name
        pass

    def get_item_list(self):
        pass


class csfloat_item_parser(item_parser):

    def get_item_list(self):
        jsonData = jsonModules.get_json_csfloat()

        # Get all item names
        options = []
        for i in jsonData['data']:

            # Create new item
            item = classes.Item()

            item.id = i['id']
            item.name = i['item']['market_hash_name']
            item.float_val = i['item'].get('float_value')
            item.paint_seed = i['item'].get('paint_seed')
            item.price_latest = i['price']/100
            item.currency = "USD"
            item.price_sold = None
            item.vendor = "CS Float"
            item.offer_type = i['type']
            item.check_float()

            # Stickers
            if i['item'].get('stickers') is not None:
                for i in i['item'].get('stickers'):
                    item.stickers.append(str(i.get('slot'))+i.get('name'))

            # Name
            item_name = item.name
            shellwidth = shutil.get_terminal_size().columns - len(item_name) - \
                len(" Steam ")
            item_name += " " * shellwidth

            # Service
            item_name += item.vendor + "\n"

            # Pricing
            item_name += str(item.price_latest) + " " + str(item.currency)

            # Offer type
            item_name += "    " + item.offer_type

            item.header = item_name
            config.item_list.append(item)
            options.append(item_name)

        return options


class steam_item_parser(item_parser):

    def get_item_list(self):
        url = f"https://steamcommunity.com/market/search?appid=730&q={
            config.curr_item}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the needed headers
        items = soup.find_all('span', class_='market_listing_item_name')
        prices = soup.find_all('span', attrs={"class": "normal_price"})

        # Exclude wrong price headers
        tp = []
        for i in prices:
            if '\n' not in i:
                tp.append(i)

        # Zip items
        item_dict = dict(zip(items, tp))
        options = []
        for i in items:
            # Get price from dict
            price = item_dict[i].text.strip()
            price = price.strip(',')

            try:
                if float(price[1:-4]) == 0.0:
                    continue
            except:
                continue

            # Create new item
            item = classes.Item()

            item.id = 0
            item.name = i.text
            item.float_val = 0
            item.paint_seed = 0
            item.price_latest = float(price[1:-4])
            item.currency = "USD"
            item.price_sold = None
            item.vendor = "Steam"
            item.offer_type = "buy_now"

            # Name
            item_name = item.name
            shellwidth = shutil.get_terminal_size().columns - len(item_name) - \
                len(" Steam ")
            item_name += " " * shellwidth

            # Service
            item_name += item.vendor + "\n"

            # Pricing
            item_name += str(item.price_latest) + " " + str(item.currency)

            # Offer type
            item_name += "    " + item.offer_type

            item.header = item_name
            config.item_list.append(item)
            options.append(item_name)

        return options

    def get_steam_price(self):
        url = f"https://steamcommunity.com/market/listings/730/Glock-18 | Warhawk (Well-Worn)"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the needed headers
        prices = soup.find_all(
            'span', class_='market_listing_price market_listing_price_with_fee')
        prices_bo = soup.find_all(
            'span', class_='market_commodity_orders_header_promote')

        # Exclude wrong price headers
        tp = []
        for i in prices:
            if '\n' not in i:
                tp.append(i)

        curr_price = float(tp[0].text.strip()[:-2].replace(',', '.'))
        print(curr_price)

        for i in prices_bo:
            print(i)
        input(" ")


# Parser objects
csfloat = csfloat_item_parser("CS Float")
steam = steam_item_parser("Steam")

# Parser dict
parser_dict = {
    0: csfloat,
    1: steam
}

parsers = [csfloat]
