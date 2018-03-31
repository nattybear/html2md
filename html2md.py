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
b = p.sub('<h2>\g<1></ht><hr>', b)

# br
b = b.replace('\n', '<br>')

# create html file
f = open('result.html', 'w')
f.write(b)
f.close()

print('[*] html file is created.')
