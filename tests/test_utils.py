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
    os.environ["FANDOM_LINK"] = "http://localhost:8080/"
    os.environ["MAX_DISTANCE"] = "2"
    assert ("[Showman](http://localhost:8080/Showman) (Uncommon Joker)" in build_reply_with_items(["showman"])) is True
    assert ("[Showman](http://localhost:8080/Showman) (Uncommon Joker)" in build_reply_with_items(["showman", "perkeo"])
            and "[Perkeo](http://localhost:8080/Perkeo) (Legendary Joker)" in build_reply_with_items(["showman", "perkeo"])) is True
    assert ("[Cavendish](http://localhost:8080/Cavendish) (Common Joker)" in build_reply_with_items(["caevendishh"])) is True
    assert ("" == build_reply_with_items([]))
    assert ("[Overstock](http://localhost:8080/Vouchers) (Voucher)" in build_reply_with_items(["overstock"])) is True
    assert ("[The Magician](http://localhost:8080/Tarot_Cards) (Tarot Card)" in build_reply_with_items(["magician"])) is True
    assert ("[Ankh](http://localhost:8080/Spectral_Cards) (Spectral Card)" in build_reply_with_items(["ankh"])) is True
    assert ("[The Arm](http://localhost:8080/Blinds_and_Antes) (Blind)" in build_reply_with_items(["arm"])) is True
    assert ("[Eris](http://localhost:8080/Planet_Cards) (Planet Card)" in build_reply_with_items(["eris"])) is True
    assert ("[Gros Michel](http://localhost:8080/Gros_Michel) (Common Joker)" in build_reply_with_items(["banana"])) is True
    assert ("[Wee Joker](http://localhost:8080/Wee_Joker) (Rare Joker)" in build_reply_with_items(["wee"])) is True
    assert ("[Joker Stencil](http://localhost:8080/Joker_Stencil) (Uncommon Joker)" in build_reply_with_items(["stencil"])) is True
    assert ("[Turtle Bean](http://localhost:8080/Turtle_Bean) (Uncommon Joker)" in build_reply_with_items(["bean"])) is True
    assert ("[Wily Joker](http://localhost:8080/Wily_Joker) (Common Joker)" in build_reply_with_items(["wily"])) is True
    assert ("[Cloud 9](http://localhost:8080/Cloud_9) (Uncommon Joker)" in build_reply_with_items(["cloud nine"])) is True
