'''

Part of "can be replaced" analysis

Opens "badFiles.txt" and looks for potential replacements (files with matching name) in "files_gva.txt" and "files_ita.txt"

'''


import os

bads = []
gva = []
ita = []

with open('badFiles.txt','r') as f:
	for lines in f:
		bads.append(lines)
with open('files_gva.txt','r') as g:
	for lines in g:
		gva.append(lines)
with open('files_ita.txt','r') as h:
	for lines in h:
		ita.append(lines)

dupli_gva = []
dupli_ita = []
for i in xrange(len(bads)):
	base = os.path.split(bads[i])[1]
	
	for x in gva:
		if os.path.split(x)[1] == base:
			dupli_gva.append(x)
	for y in ita:
		if os.path.split(y)[1] == base:
			dupli_ita.append(y)

with open('found_gva.txt','w') as f:
	for item in dupli_gva:
		f.write(item)
with open('found_ita.txt','w') as g:
	for item in dupli_ita:
		g.write(item)

bases = [os.path.split(x)[1] for x in dupli_gva]
total = [x for x in dupli_gva]
for y in dupli_ita:
	if os.path.split(y)[1] not in bases:
		total.append(y)

with open('found_all.txt','w') as h:
	for item in total:
		h.write(item)

