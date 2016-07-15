#!/usr/bin/env python
"""
Usage:
    pandoc --filter ./minted.py -o myfile.tex myfile.md
"""
import os

from pandocfilters import toJSONFilter, RawBlock, RawInline


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

        # convert our parameters to minted options
        options = []
        for key in params:
            options.append("%s=%s" % (key, params[key]))

        params = ", ".join(options)

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
                content = r'\inputminted[' + params + ']{' + language + '}{' + source_file + '}'
                return [RawBlock(format, content)]

        elif key == 'Code':
            body, language, params, source_file = unpack(value, meta)

            if language is None:
                return

            html = '<code class="language-%s">%s</code>' % (language, body)
            return [RawInline(format, html)]


if __name__ == '__main__':
    import sys

    #sys.stdout = open("bubber.html", "w")
    #sys.stdin = open("test.json")
    toJSONFilter(prism)
