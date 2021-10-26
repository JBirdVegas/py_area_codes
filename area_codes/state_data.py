import typing

from area_codes.data_types import UsStateAbbreviation, UsState, AreaCode, AreaCodes

area_codes_to_state: typing.Dict[AreaCode, UsState] = {
    205: "alabama", 251: "alabama", 256: "alabama", 334: "alabama", 659: "alabama", 938: "alabama",
    907: "alaska",
    480: "arizona", 520: "arizona", 602: "arizona", 623: "arizona", 928: "arizona",
    479: "arkansas", 501: "arkansas", 870: "arkansas",

    209: "california", 213: "california", 279: "california", 310: "california", 323: "california", 341: "california",
    408: "california", 415: "california", 424: "california", 442: "california", 510: "california", 530: "california",
    559: "california", 562: "california", 619: "california", 626: "california", 628: "california", 650: "california",
    657: "california", 661: "california", 669: "california", 707: "california", 714: "california", 747: "california",
    760: "california", 805: "california", 818: "california", 820: "california", 831: "california", 858: "california",
    909: "california", 916: "california", 925: "california", 949: "california", 951: "california",

    303: "colorado", 719: "colorado", 720: "colorado", 970: "colorado",
    203: "connecticut", 475: "connecticut", 860: "connecticut", 959: "connecticut",
    302: "delaware",

    239: "florida", 305: "florida", 321: "florida", 352: "florida", 386: "florida", 407: "florida", 561: "florida",
    689: "florida", 727: "florida", 754: "florida", 772: "florida", 786: "florida", 813: "florida", 850: "florida",
    863: "florida", 904: "florida", 941: "florida", 954: "florida",

    229: "georgia", 404: "georgia", 470: "georgia", 478: "georgia", 678: "georgia", 706: "georgia", 762: "georgia",
    770: "georgia", 912: "georgia",

    808: "hawaii",

    217: "illinois", 224: "illinois", 309: "illinois", 312: "illinois", 331: "illinois", 618: "illinois",
    630: "illinois", 708: "illinois", 773: "illinois", 779: "illinois", 815: "illinois", 847: "illinois",
    872: "illinois",

    219: "indiana", 260: "indiana", 317: "indiana", 463: "indiana", 574: "indiana", 765: "indiana", 812: "indiana",
    930: "indiana",

    319: "iowa", 515: "iowa", 563: "iowa", 641: "iowa", 712: "iowa",
    316: "kansas", 620: "kansas", 785: "kansas", 913: "kansas",
    270: "kentucky", 364: "kentucky", 502: "kentucky", 606: "kentucky", 859: "kentucky",
    225: "louisiana", 318: "louisiana", 337: "louisiana", 504: "louisiana", 985: "louisiana",
    207: "maine",
    227: "maryland", 240: "maryland", 301: "maryland", 410: "maryland", 443: "maryland", 667: "maryland",

    339: "massachusetts", 351: "massachusetts", 413: "massachusetts", 508: "massachusetts", 617: "massachusetts",
    774: "massachusetts", 781: "massachusetts", 857: "massachusetts", 978: "massachusetts",

    231: "michigan", 248: "michigan", 269: "michigan", 313: "michigan", 517: "michigan", 586: "michigan",
    616: "michigan", 734: "michigan", 810: "michigan", 906: "michigan", 947: "michigan", 989: "michigan",

    218: "minnesota", 320: "minnesota", 507: "minnesota", 612: "minnesota", 651: "minnesota", 763: "minnesota",
    952: "minnesota",

    228: "mississippi", 601: "mississippi", 662: "mississippi", 769: "mississippi",
    314: "missouri", 417: "missouri", 573: "missouri", 636: "missouri", 660: "missouri", 816: "missouri",
    406: "montana",
    308: "nebraska", 402: "nebraska", 531: "nebraska",
    702: "nevada", 725: "nevada", 775: "nevada",
    603: "new hampshire",

    201: "new jersey", 551: "new jersey", 609: "new jersey", 640: "new jersey", 732: "new jersey", 848: "new jersey",
    856: "new jersey", 862: "new jersey", 908: "new jersey", 973: "new jersey",

    505: "new mexico", 575: "new mexico",

    212: "new york", 315: "new york", 332: "new york", 347: "new york", 516: "new york", 518: "new york",
    585: "new york", 607: "new york", 631: "new york", 646: "new york", 680: "new york", 716: "new york",
    718: "new york", 838: "new york", 845: "new york", 914: "new york", 917: "new york", 929: "new york",
    934: "new york",

    252: "north carolina", 336: "north carolina", 704: "north carolina", 743: "north carolina", 828: "north carolina",
    910: "north carolina", 919: "north carolina", 980: "north carolina", 984: "north carolina",

    701: "north dakota",

    216: "ohio", 220: "ohio", 234: "ohio", 283: "ohio", 326: "ohio", 330: "ohio", 380: "ohio", 419: "ohio", 440: "ohio",
    513: "ohio", 567: "ohio", 614: "ohio", 740: "ohio", 937: "ohio",

    405: "oklahoma", 539: "oklahoma", 572: "oklahoma", 580: "oklahoma", 918: "oklahoma",
    458: "oregon", 503: "oregon", 541: "oregon", 971: "oregon",

    215: "pennsylvania", 223: "pennsylvania", 267: "pennsylvania", 272: "pennsylvania", 412: "pennsylvania",
    445: "pennsylvania", 484: "pennsylvania", 570: "pennsylvania", 610: "pennsylvania", 717: "pennsylvania",
    724: "pennsylvania", 814: "pennsylvania", 878: "pennsylvania",

    401: "rhode island",
    803: "south carolina", 839: "south carolina", 843: "south carolina", 854: "south carolina", 864: "south carolina",
    605: "south dakota",

    423: "tennessee", 615: "tennessee", 629: "tennessee", 731: "tennessee", 865: "tennessee", 901: "tennessee",
    931: "tennessee",

    210: "texas", 214: "texas", 254: "texas", 281: "texas", 325: "texas", 346: "texas", 361: "texas", 409: "texas",
    430: "texas", 432: "texas", 469: "texas", 512: "texas", 682: "texas", 713: "texas", 726: "texas", 737: "texas",
    806: "texas", 817: "texas", 830: "texas", 832: "texas", 903: "texas", 915: "texas", 936: "texas", 940: "texas",
    956: "texas", 972: "texas", 979: "texas",

    385: "utah", 435: "utah", 801: "utah",
    802: "vermont",

    276: "virginia", 434: "virginia", 540: "virginia", 571: "virginia", 703: "virginia", 757: "virginia",
    804: "virginia",

    206: "washington", 253: "washington", 360: "washington", 425: "washington", 509: "washington", 564: "washington",
    202: "washington dc",
    304: "west virginia", 681: "west virginia",
    262: "wisconsin", 414: "wisconsin", 534: "wisconsin", 608: "wisconsin", 715: "wisconsin", 920: "wisconsin",
    307: "wyoming",
    684: "american samoa",
    671: "guam",
    670: "marianas island",
    787: "puerto rico", 939: "puerto rico",
    340: "us virgin islands"
}

state_to_area_code: typing.Dict[UsState, AreaCodes] = {
    "alabama": [
        205, 251, 256, 334, 659, 938
    ],
    "alaska": [907],
    "arizona": [
        480, 520, 602, 623, 928
    ],
    "arkansas": [
        479, 501, 870
    ],
    "california": [
        209, 213, 279, 310, 323, 341, 408, 415, 424, 442,
        510, 530, 559, 562, 619, 626, 628, 650, 657, 661,
        669, 707, 714, 747, 760, 805, 818, 820, 831, 858,
        909, 916, 925, 949, 951
    ],
    "colorado": [
        303, 719, 720, 970
    ],
    "connecticut": [
        203, 475, 860, 959
    ],
    "delaware": [302],
    "florida": [239, 305, 321, 352, 386, 407, 561, 689, 727, 754, 772, 786, 813, 850, 863, 904, 941, 954],
    "georgia": [229, 404, 470, 478, 678, 706, 762, 770, 912],
    "hawaii": [808],
    "illinois": [217, 224, 309, 312, 331, 618, 630, 708, 773, 779, 815, 847, 872],
    "indiana": [219, 260, 317, 463, 574, 765, 812, 930],
    "iowa": [319, 515, 563, 641, 712],
    "kansas": [316, 620, 785, 913],
    "kentucky": [270, 364, 502, 606, 859],
    "louisiana": [225, 318, 337, 504, 985],
    "maine": [207],
    "maryland": [227, 240, 301, 410, 443, 667],
    "massachusetts": [339, 351, 413, 508, 617, 774, 781, 857, 978],
    "michigan": [231, 248, 269, 313, 517, 586, 616, 734, 810, 906, 947, 989],
    "minnesota": [218, 320, 507, 612, 651, 763, 952],
    "mississippi": [228, 601, 662, 769],
    "missouri": [314, 417, 573, 636, 660, 816],
    "montana": [406],
    "nebraska": [308, 402, 531],
    "nevada": [702, 725, 775],
    "new hampshire": [603],
    "new jersey": [201, 551, 609, 640, 732, 848, 856, 862, 908, 973],
    "new mexico": [505, 575],
    "new york": [212, 315, 332, 347, 516, 518, 585, 607, 631, 646, 680, 716, 718, 838, 845, 914, 917, 929, 934],
    "north carolina": [252, 336, 704, 743, 828, 910, 919, 980, 984],
    "north dakota": [701],
    "ohio": [216, 220, 234, 283, 326, 330, 380, 419, 440, 513, 567, 614, 740, 937],
    "oklahoma": [405, 539, 572, 580, 918],
    "oregon": [458, 503, 541, 971],
    "pennsylvania": [215, 223, 267, 272, 412, 445, 484, 570, 610, 717, 724, 814, 878],
    "rhode island": [401],
    "south carolina": [803, 839, 843, 854, 864],
    "south dakota": [605],
    "tennessee": [423, 615, 629, 731, 865, 901, 931],
    "texas": [
        210, 214, 254, 281, 325, 346, 361, 409, 430, 432, 469, 512, 682,
        713, 726, 737, 806, 817, 830, 832, 903, 915, 936, 940, 956, 972, 979
    ],
    "utah": [385, 435, 801],
    "vermont": [802],
    "virginia": [276, 434, 540, 571, 703, 757, 804],
    "washington": [206, 253, 360, 425, 509, 564],
    "washington dc": [202],
    "west virginia": [304, 681],
    "wisconsin": [262, 414, 534, 608, 715, 920],
    "wyoming": [307],
    "american samoa": [684],
    "guam": [671],
    "marianas island": [670],
    "puerto rico": [787, 939],
    "us virgin islands": [340]
}

state_to_abbrev: typing.Dict[UsState, UsStateAbbreviation] = {
    "alabama": "al",
    "alaska": "ak",
    "arizona": "az",
    "arkansas": "ar",
    "california": "ca",
    "colorado": "co",
    "connecticut": "ct",
    "delaware": "de",
    "florida": "fl",
    "georgia": "ga",
    "hawaii": "hi",
    "idaho": "id",
    "illinois": "il",
    "indiana": "in",
    "iowa": "ia",
    "kansas": "ks",
    "kentucky": "ky",
    "louisiana": "la",
    "maine": "me",
    "maryland": "md",
    "massachusetts": "ma",
    "michigan": "mi",
    "minnesota": "mn",
    "mississippi": "ms",
    "missouri": "mo",
    "montana": "mt",
    "nebraska": "ne",
    "nevada": "nv",
    "new hampshire": "nh",
    "new jersey": "nj",
    "new mexico": "nm",
    "new york": "ny",
    "north carolina": "nc",
    "north dakota": "nd",
    "ohio": "oh",
    "oklahoma": "ok",
    "oregon": "or",
    "pennsylvania": "pa",
    "rhode island": "ri",
    "south carolina": "sc",
    "south dakota": "sd",
    "tennessee": "tn",
    "texas": "tx",
    "utah": "ut",
    "vermont": "vt",
    "virginia": "va",
    "washington": "wa",
    "west virginia": "wv",
    "wisconsin": "wi",
    "wyoming": "wy",
    "washington dc": "dc",
    "american samoa": "as",
    "guam": "gu",
    "mariana islands": "mp",
    "puerto rico": "pr",
    "us virgin islands": "vi",
}

abbrev_to_state: typing.Dict[UsStateAbbreviation, UsState] = {
    abbrev: state
    for state, abbrev in state_to_abbrev.items()
}
