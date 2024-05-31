class dictionary:

    cld_amts = {  # Things in this list appear with cloud heights (3 Numbers - [REGEX(\D\D\D\d\d\d]) immediately after the abbreviation
        "FEW": "\nFew Clouds at ",
        "SCT": "\nScattered Cloud at ",
        "BKN": "\nBroken Cloud at ",
        "OVC": "\nOvercast Cloud at ",
    }

    cld_types = {"CB": "Cumulonimbus", "TCU": "Towering Cumulus"}

    acronyms = {  # Things in this list appear by themselves with clear spaces either side of the words [REGEX(\Wxxxxx\W)]
        "YPDN": "\nDarwin",
        "METAR": "\nMeteorological Aerodrome Report",
        "RMK": "\n---Remarks:",
        "RWY": "Runway",
        "SPECI": "\nSpecial Report",
        "CAVOK": "\nCeiling and Visibility OK",
        "NSC": "\nNil Significant Cloud",
        "SKC": "\nSky Clear",
        "NSW": "\nNo Significant Weather",
    }

    wind = {
        "VRB": "variable wind at ",
        "KT": "Knots",
        "005": "5 degrees",
        "010": "10 Degrees",
    }

    weather = {
        "BR": "Mist",
        "DS": "Dust Storm",
        "DU": "Dust",
        "DZ": "Drizzle",
        "FG": "Fog",
        "FU": "Smoke",
        "FZ": "Freezing",
        "GR": "Hail",
        "HZ": "Haze",
        "RA": "Rain",
        "SA": "Sand",
        "SH": "Showers",
        "SN": "Snow",
        "SQ": "Squalls",
        "SS": "Sandstorm",
        "TS": "Thunderstorm",
        "VA": "Volcanic Ash",
        "VC": "In the vicinity",
    }
