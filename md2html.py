#!/usr/bin/python3

from sys import argv
from re import compile

def md2html(md):

    # quote box
    p = compile('> (.*)')
    md = p.sub("<div style='border-left: 10px solid lightgray; padding: 20px;'>\g<1></div>", md)

    # h2
    p = compile('## (.*)')
    md = p.sub('<h2>\g<1></h2><hr>', md)

    # bold
    p = compile('[*](.*?)[*]')
    md = p.sub('<b>\g<1></b>', md)

    # strike
    p = compile('[~](.*?)[~]')
    md = p.sub('<strike>\g<1></strike>', md)

    # br
    md = md.replace('\n', '<br>')

    # multi-line code
    p = compile('```(.*?)```')
    md = p.sub("<div style='background-color: lightgray;'>\g<1></div>", md)

    # code
    p = compile('`(.*?)`')
    md = p.sub("<span style='background-color: lightgray;'>\g<1></span>", md)

    return md

if __name__ == '__main__':

    if len(argv) != 2:
        print('usage : html2md [filename]')
        exit()

    filename = argv[1]
    f = open(filename)
    md = f.read()
    f.close()
    filename = ''.join(filename.split('.')[:-1])
    filename = filename + '.html'
    html = md2html(md)
    charset = "<meta charset='utf-8'>"
    html = charset + html
    f = open(filename, 'w')
    f.write(html)
    f.close()

    print('[*] html file is created!')
