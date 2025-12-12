from modules.jokers import jokers
from modules.blinds import blinds
from modules.spectrals import spectrals
from modules.tarots import tarots
from modules.vouchers import vouchers
from modules.planets import planets
from modules.decks import decks
from modules.stakes import stakes
from Levenshtein import distance
import time
import os
import re

def build_reply_with_items(items_from_comment):
    matches_per_item = {}
    levenshtein_start = time.time()

    for requested_item in items_from_comment:
        for key, value in (jokers | blinds | spectrals | tarots | vouchers | planets | decks | stakes).items():
            item_distance = distance(format_item(value["name"]), format_item(requested_item), score_cutoff=int(os.environ["MAX_DISTANCE"]))
            if item_distance <= int(os.environ["MAX_DISTANCE"]):
                if not requested_item in matches_per_item:
                    matches_per_item[requested_item] = []
                matches_per_item[requested_item].append({ "key": key, "match": value, "distance": item_distance })
    levenshtein_end = time.time()
    print(f"Fuzzy string matching for all items took: {levenshtein_end - levenshtein_start} seconds")
    reply = ""
    matches = 0
    for key, value in matches_per_item.items():
        value.sort(key=lambda x: x["distance"])
        reply += (
            f"[{value[0]['match']['name']}]({get_link(value[0])})"
            f" ({get_item_label(value[0])})\n"
            f"- **Effect**: {value[0]['match']['text']}\n"
            f"{get_item_unlock(value[0])}"
        )
        matches += 1
    if (matches > 0):
        reply += '[^(Source)](https://github.com/AlecM33/balatro-joker-bot)'

    return reply

def parse_items_from_comment(comment):
    return re.findall(r"[\\]?\[[\\]?\[([^][\\]+?)[\\]?\][\\]?\]", comment)


def get_item_label(value):
    if value["key"].startswith("j_"):
        if ("rarity" in value["match"]):
            return f"{value['match']['rarity']} Joker"
        else:
            return "Common Joker"
    elif value["key"].startswith("bl_"):
        return "Blind"
    elif value["key"].startswith("s_"):
        return "Spectral Card"
    elif value["key"].startswith("t_"):
        return "Tarot Card"
    elif value["key"].startswith("v_"):
        return "Voucher"
    elif value["key"].startswith("p_"):
        return "Planet Card"
    elif value["key"].startswith("d_"):
        return "Deck"
    elif value["key"].startswith("st_"):
        return "Stake"
    else:
        return "Unknown"

def get_item_unlock(value):
    if value["key"].startswith("j_") or value["key"].startswith("v_") or value["key"].startswith("d_"):
        return f"- **To Unlock**: {value['match']['unlock'] if 'unlock' in value['match'] else 'Available by default'}\n\n"
    elif value["key"].startswith("st_"):
        return f"- **Unlocks on Win**: {value['match']['unlocks'] if 'unlocks' in value['match'] else 'None'}\n\n"
    else:
        return f"\n"


def get_link(value):
    return os.environ['WIKI_LINK'] + value["match"]["name"].replace(" ", "_")

def format_item(item):
    nickname_map = { # some nicknames/variations seen around the subreddit.
        "banana": "gros michel",
        "oops! all sixes": "oops! all 6s",
        "oops, all sixes": "oops! all 6s",
        "oops all sixes": "oops! all 6s",
        "eight ball": "8 ball",
        "cloud nine": "cloud 9",
        "bean": "turtle bean",
        "jonkler": "joker",
        "jimbo": "joker",
        "cat": "lucky cat",
        "sock": "sock and buskin",
        "sock n buskin": "sock and buskin",
        "stencil": "joker stencil",
        "pants": "spare trousers",
        "spare pants": "spare trousers",
        "trib": "triboulet",
        "vessel": "violet vessel",
    }
    item = item.lower().strip().removeprefix("the ").removesuffix(" joker")
    return nickname_map.get(item, item)
