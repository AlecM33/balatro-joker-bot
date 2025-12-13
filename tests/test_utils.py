from modules.utils import build_reply_with_items, parse_items_from_comment
import os

def test_parse_items_from_comment():
    assert ["baron"] == parse_items_from_comment("Use [[baron]]")
    assert ["baron", "mime"] == parse_items_from_comment("Use [[baron]] and [[mime]]")
    assert ["baron", "mime"] == parse_items_from_comment("Use \\[\\[baron\\]\\] and \\[\\[mime\\]\\]")
    assert ["baron", "mime"] == parse_items_from_comment("Use \\[[baron]] and \\[[mime]]")
    assert ["mime"] == parse_items_from_comment("Use [[baron] and [[mime]]")
    assert ["baron", "mime"] == parse_items_from_comment("Use [[baron]][[mime]]")
    assert ["baron", "mime"] == parse_items_from_comment("Use [[[baron]]][[[mime]]]")
    assert ["baron", "mime"] == parse_items_from_comment("Use [[baron]], [[]], and [[mime]]")
    assert [] == parse_items_from_comment("[[]], [[]]")

def test_build_reply_with_items():
    os.environ["WIKI_LINK"] = "http://localhost:8080/"
    os.environ["MAX_DISTANCE"] = "2"
    assert ("[Showman](http://localhost:8080/Showman) (Uncommon Joker)" in build_reply_with_items(["showman"])) is True
    assert ("[Showman](http://localhost:8080/Showman) (Uncommon Joker)" in build_reply_with_items(["showman", "perkeo"])
            and "[Perkeo](http://localhost:8080/Perkeo) (Legendary Joker)" in build_reply_with_items(["showman", "perkeo"])) is True
    assert ("[Cavendish](http://localhost:8080/Cavendish) (Common Joker)" in build_reply_with_items(["caevendishh"])) is True
    assert ("" == build_reply_with_items([]))
    assert ("[Overstock](http://localhost:8080/Overstock) (Voucher)" in build_reply_with_items(["overstock"])) is True
    assert ("[The Magician](http://localhost:8080/The_Magician) (Tarot Card)" in build_reply_with_items(["magician"])) is True
    assert ("[Ankh](http://localhost:8080/Ankh) (Spectral Card)" in build_reply_with_items(["ankh"])) is True
    assert ("[The Arm](http://localhost:8080/The_Arm) (Blind)" in build_reply_with_items(["arm"])) is True
    assert ("[Eris](http://localhost:8080/Eris) (Planet Card)" in build_reply_with_items(["eris"])) is True
    assert ("[Gros Michel](http://localhost:8080/Gros_Michel) (Common Joker)" in build_reply_with_items(["banana"])) is True
    assert ("[Wee Joker](http://localhost:8080/Wee_Joker) (Rare Joker)" in build_reply_with_items(["wee"])) is True
    assert ("[Joker Stencil](http://localhost:8080/Joker_Stencil) (Uncommon Joker)" in build_reply_with_items(["stencil"])) is True
    assert ("[Turtle Bean](http://localhost:8080/Turtle_Bean) (Uncommon Joker)" in build_reply_with_items(["bean"])) is True
    assert ("[Wily Joker](http://localhost:8080/Wily_Joker) (Common Joker)" in build_reply_with_items(["wily"])) is True
    assert ("[Cloud 9](http://localhost:8080/Cloud_9) (Uncommon Joker)" in build_reply_with_items(["cloud nine"])) is True
    assert ("[Red Deck](http://localhost:8080/Red_Deck) (Deck)" in build_reply_with_items(["red deck"])) is True
    assert ("[Plasma Deck](http://localhost:8080/Plasma_Deck) (Deck)" in build_reply_with_items(["plasma deck"])) is True
    assert ("[Ghost Deck](http://localhost:8080/Ghost_Deck) (Deck)" in build_reply_with_items(["ghost deck"])) is True

    # Stakes
    assert ("[White Stake](http://localhost:8080/White_Stake) (Stake)" in build_reply_with_items(["white stake"])) is True
    assert ("[Red Stake](http://localhost:8080/Red_Stake) (Stake)" in build_reply_with_items(["red stake"])) is True
    assert ("[Green Stake](http://localhost:8080/Green_Stake) (Stake)" in build_reply_with_items(["green stake"])) is True
    assert ("[Black Stake](http://localhost:8080/Black_Stake) (Stake)" in build_reply_with_items(["black stake"])) is True
    assert ("[Blue Stake](http://localhost:8080/Blue_Stake) (Stake)" in build_reply_with_items(["blue stake"])) is True
    assert ("[Purple Stake](http://localhost:8080/Purple_Stake) (Stake)" in build_reply_with_items(["purple stake"])) is True
    assert ("[Orange Stake](http://localhost:8080/Orange_Stake) (Stake)" in build_reply_with_items(["orange stake"])) is True
    assert ("[Gold Stake](http://localhost:8080/Gold_Stake) (Stake)" in build_reply_with_items(["gold stake"])) is True

    assert ("[Bonus Cards](http://localhost:8080/Bonus_Cards) (Enhancement)" in build_reply_with_items(["bonus card"])) is True
    assert ("[Mult Cards](http://localhost:8080/Mult_Cards) (Enhancement)" in build_reply_with_items(["mult card"])) is True
    assert ("[Wild Cards](http://localhost:8080/Wild_Cards) (Enhancement)" in build_reply_with_items(["wild card"])) is True
    assert ("[Glass Cards](http://localhost:8080/Glass_Cards) (Enhancement)" in build_reply_with_items(["glass card"])) is True
    assert ("[Steel Cards](http://localhost:8080/Steel_Cards) (Enhancement)" in build_reply_with_items(["steel card"])) is True
    assert ("[Stone Cards](http://localhost:8080/Stone_Cards) (Enhancement)" in build_reply_with_items(["stone card"])) is True
    assert ("[Gold Cards](http://localhost:8080/Gold_Cards) (Enhancement)" in build_reply_with_items(["gold card"])) is True
    assert ("[Lucky Cards](http://localhost:8080/Lucky_Cards) (Enhancement)" in build_reply_with_items(["lucky card"])) is True
