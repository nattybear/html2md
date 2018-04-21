#!/usr/bin/python3

from sys import argv
from re import compile
from tkinter import Tk

def set_clipboard(html):
    root = Tk()
    root.clipboard_clear()
    root.clipboard_append(html)
    root.mainloop()

def md2html(md):
    # h2
    p = compile('## (.*)')
    md = p.sub('<h2>\g<1></h2><hr>', md)

    # bold
    p = compile('[*](.*?)[*]')
    md = p.sub('<b>\g<1></b>', md)

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

    f = open(argv[1])
    md = f.read()
    f.close()

    html = md2html(md)

    set_clipboard(html)
