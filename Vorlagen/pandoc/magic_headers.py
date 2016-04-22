#!/usr/bin/env python3
"""
Usage:
    pandoc --filter ./magic_headers.py  myfile.md -o myfile.tex
"""
import sys
from pandocfilters import toJSONFilter, RawBlock, RawInline


def insert_break(format, options):
    return [RawBlock(format, "\pagebreak")]


template_minipage_start = r"""\begin{minipage}[t]{%.2f\textwidth}
\vspace{0pt}
"""
template_minipage_end = r"""\end{minipage}\vspace{12pt}"""


def minipage_start(format, options):
    global split_status
    w = float(options.get("w", .5))
    content = template_minipage_start % w
    return RawBlock(format, content)


def minipage_next(format, options):
    w = float(options.get("w", .5))
    content = template_minipage_end + (template_minipage_start % w)
    return RawBlock(format, content)


def minipage_end(format, options):
    content = template_minipage_end
    return RawBlock(format, content)


MAGIC_OPTIONS = {
    "break": insert_break,
    "minipageStart": minipage_start,
    "minipageEnd": minipage_end,
    "minipageNext": minipage_next
}

center_template = r"""{\centering
\includegraphics[width=\maxwidth{%.2f\textwidth}]{%s}"""
caption_template = r"""\captionof{figure}{%s}}"""


def center_image(image_path, caption, width):
    tex = center_template % (width, image_path) + r"\vspace{5pt}"
    if caption is not None and len(caption) > 0:
        return tex + caption_template % caption + r"\vspace{5pt}"

    return tex


def parse(key, value, format, meta):
    if format == 'latex':

        if key == 'Image':
            options = {key: val for key, val in value[0][2]}
            image_name = value[2][0]
            width = float(options.get("w", .9))

            caption = None
            if len(value[1]) > 0:
                capt = value[1]
                caption = ""
                for part in capt:
                    if part["t"] == "Str":
                        caption += part["c"]
                    elif part["t"] == "Space":
                        caption += " "


            content = center_image(image_name, caption, width)
            return [RawInline(format, content)]

        if key == 'Header' and len(value[1][2]) > 0:
            options = {key: val for key, val in value[1][2]}
            if "magic" in options and options["magic"] in MAGIC_OPTIONS:
                magic_func = MAGIC_OPTIONS[options["magic"]]
                return magic_func(format, options)


if __name__ == '__main__':
    #sys.stdin = open("test.json") # testing only
    toJSONFilter(parse)
