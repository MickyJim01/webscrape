import re
from icecream import ic
from clouds import dictionary as dc


def plain_text(taf):

    new = re.sub("METAR", "Meteorological Aeordrome Report", taf)

    return new


def translate(briefing):
    dict = {
        "YPDN": "Darwin",
        "METAR": "Meteorological Aerodrome Report",
        "RMK": "Remarks:",
        "FEW": "Few Clouds at ",
    }

    brief_words = briefing.split()
    for i, word in enumerate(brief_words):
        if word in dict:
            brief_words[i] = dict[word]

    return " ".join(brief_words)


def re_trans(briefing):
    dict = dc.cld_amts
    ic(dict)

    for k, v in ic(dict.items()):
        briefing = ic(re.sub(rf"(\s){k}(\d\d\d\s)", rf"\1{v}\2", briefing))
    return briefing
