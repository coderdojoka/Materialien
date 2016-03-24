#!/usr/bin/env python
"""
A pandoc filter that has the LaTeX writer use minted for typesetting code.
Based on: https://github.com/nick-ulle/pandoc-minted
Original license: https://github.com/nick-ulle/pandoc-minted/blob/master/LICENSE

Usage:
    pandoc --filter ./minted.py -o myfile.tex myfile.md
"""

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


def minted(key, value, format, meta):
    """ Use minted for code in LaTeX.

    Args:
        key:     type of pandoc object
        value:   contents of pandoc object
        format:  target output format
        meta:    document metadata
    """
    if format == 'latex':

        if key == 'CodeBlock':
            body, language, params, source_file = unpack(value, meta)
            if language is None:
                return

            if source_file is None:
                begin = r'\begin{minted}[' + params + ']{' + language + '}\n'
                end = '\n' + r'\end{minted}'
                return [RawBlock(format, begin + body + end)]

            else:
                content = r'\inputminted[' + params + ']{' + language + '}{' + source_file + '}'
                return [RawBlock(format, content)]

        elif key == 'Code':
            body, language, params, source_file = unpack(value, meta)

            if language is None:
                return

            begin = r'\mintinline[' + params + ']{' + language + '}{'
            end = '}'

            return [RawInline(format, begin + body + end)]


if __name__ == '__main__':
    toJSONFilter(minted)
