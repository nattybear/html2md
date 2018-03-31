#!/usr/bin/python3

from sys import argv
from re import compile

if len(argv) != 2:
	print('usage : html2md [filename]')
	exit()

f = open(argv[1])
b = f.read()
f.close()

# h2
p = compile('^## (.*)')
b = p.sub('<h2>\g<1></h2><hr>', b)

# br
b = b.replace('\n', '<br>')

# code
p = compile('`(.*?)`')
b = p.sub('<span style="background-color: lightgray;">\g<1></span>', b)

# create html file
f = open('result.html', 'w')
f.write(b)
f.close()

print('[*] html file is created.')
