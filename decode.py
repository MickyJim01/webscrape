import re
from icecream import ic
from dictionary import dictionary as dc


def plain_text(taf):

    new = re.sub("METAR", "Meteorological Aeordrome Report", taf)

    return new


def translate(briefing):
    dict = {
        "YPDN": "\nDarwin",
        "METAR": "\nMeteorological Aerodrome Report",
        "RMK": "\n---Remarks:",
    }

    brief_words = briefing.split()
    for i, word in enumerate(brief_words):
        if word in dict:
            brief_words[i] = dict[word]

    return " ".join(brief_words)


# Translate the breifing using regular expressions.
# this function only translates cloud amounts using the 'cloud amounts' dictionary
def re_trans(briefing):
    dict = dc.cld_amts
    dict

    for k, v in dict.items():
        briefing = re.sub(rf"(\s){k}(\d\d\d\s)", rf"\1{v}\2", briefing)
    return briefing
