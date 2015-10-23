__author__ = 'Mark Weinreuter'

zeichen_text = {
    "4-1": "a",
    "4-2": "b",
    "4-3": "c",
    "4-4": "d",
    "4-5": "e",
    "4-6": "f",
    "4-7": "g",
    "4-8": "h",
    "4-9": "i",
    "4-⚑": "j",
    "4-☂": "k",
    "4-❤": "l",
    "4-★": "m",
    "4-☢": "n",
    "4-♫": "o",
    "5-0": "p",
    "5-1": "q",
    "5-2": "r",
    "5-3": "s",
    "5-4": "t",
    "5-5": "u",
    "5-6": "v",
    "5-7": "w",
    "5-8": "x",
    "5-9": "y",
    "5-⚑": "z",
    "2-❤": ",",
    "2-☢": ".",
    " " : " "
}

text_zeichen =  {v: k for k, v in zeichen_text.items()}

text = "links, unter dem baumstamm."
konv_text = ""

for buchstabe in text:
    konv_text += text_zeichen[buchstabe]

print(konv_text)