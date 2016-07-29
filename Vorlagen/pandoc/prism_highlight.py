#!/usr/bin/env python
"""
Usage:
    pandoc --filter ./minted.py -o myfile.tex myfile.md
"""
import os
import sys

from pandocfilters import toJSONFilter, RawBlock, RawInline

ENDINGS = {"py": "python", "html": "html", "css": "css", "js": "javascript"}


def unpack(value, meta):
    """ Unpack the body and language of a pandoc code element.

    Args:
        value:   contents of pandoc object
        meta:    document metadata
    """
    [attrib, body] = value

    # default options
    params = {
        'breaklines': 'true',
        'linenumbers': 'true'
    }
    # if we want to load code from an external source file
    source = None

    try:
        [_, [language], extras] = attrib

        for [key, value] in extras:

            # special case if we want to include code from an external file
            if key == "include":
                source = value
            else:
                params[key] = value


    except ValueError:
        # Use default language, or don't highlight.
        language = meta.get('minted-language')
        if language is not None:
            language = language['c'][0]['c']

    return body, language, params, source


def prism(key, value, format, meta):
    """ Use minted for code in LaTeX.

    Args:
        key:     type of pandoc object
        value:   contents of pandoc object
        format:  target output format
        meta:    document metadata
    """

    if format == "html":
        if key == 'Image':
            import base64
            path = value[2][0]
            if not os.path.exists(path):
                print("No such image: " + path)
            encoded = "data:image/png;base64," + base64.b64encode(open(path, "rb").read()).decode()
            html = '<img alt="" src="%s">' % (encoded)
            return [RawInline(format, html)]

        if key == 'CodeBlock':
            body, language, params, source_file = unpack(value, meta)
            if language is None:
                return

            if source_file is None:
                html = '<pre><code class="language-%s">%s</code></pre>' % (language, body)
                return [RawBlock(format, html)]

            else:
                with open(source_file, 'r') as file:
                    code = file.readlines()
                lastline = len(code)
                firstline = 0
                if 'lastline' in params:
                    lastline = min(lastline, int(params['lastline']))
                if 'firstline' in params:
                    firstline = max(firstline, min(lastline, int(params['firstline'])-1))

                body = "".join(code[firstline: lastline])

                # determine language by ending
                dot_index = source_file.rindex(".")
                ending = source_file[dot_index + 1:]
                if ending not in ENDINGS:
                    raise AttributeError("Unknown ending: " + ending)
                language = ENDINGS[ending]

                html = '<pre><code class="language-%s">%s</code><pre>' % (language, body)
                return [RawBlock(format, html)]

        elif key == 'Code':
            body, language, params, source_file = unpack(value, meta)

            if language is None:
                return

            html = '<code class="language-%s">%s</code>' % (language, body)
            return [RawInline(format, html)]


if __name__ == '__main__':
    # sys.stdout = open("bubber.html", "w")
    #sys.stdin = open("test.json")
    toJSONFilter(prism)
