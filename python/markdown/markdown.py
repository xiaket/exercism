#!/usr/bin/env python
#encoding=utf8


import re

STRONG = re.compile(r'(.*?)__(.*?)__(.*?)')
EM = re.compile(r'(.*?)_(.*?)_(.*?)')


def parse_markdown(markdown):
    lines = markdown.split('\n')
    parsed = []
    res = ''
    in_list = False
    for line in lines:
        # handle strong and em.
        line = STRONG.sub('\g<1><strong>\g<2></strong>\g<3>', line)
        line = EM.sub('\g<1><em>\g<2></em>\g<3>', line)
        if line.startswith("#"):
            level = len(line.split()[0])
            line = '<h{level}>{content}</h{level}>'.format(
                level=level, content=line.split(" ", 1)[1]
            )
        elif line.startswith("* "):
            line = line.split(" ", 1)[1]
            line = '<li>' + line + '</li>'
            if not in_list:
                line = '<ul>' + line
                in_list = True
        else:
            if in_list:
                line = '</ul>' + line
                in_list = False
            line = '<p>' + line + '</p>'
        parsed.append(line)
    if in_list:
        parsed[-1] = parsed[-1] + '</ul>'

    return ''.join(parsed)
