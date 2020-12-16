import sys
from conllu import parse
from nltk import Tree
from nltk import Nonterminal, Production

#GENERATE CFG
trees=open('/Users/sykim/Desktop/train').read()
mytrees=Tree.fromstring(trees)

CFGgrammar = []
for t in mytrees:
    for x in mytrees.parsed_sents(t):
        productions += x.productions()

sentences=parse(open('/Users/sykim/Desktop/test.conllu').read())
t=[]
for sentence in sentences:
    for tokens in sentence:
        t.append(tokens)
d=[]
for item in t:
    d.append(item["form"])

pos=[]
for item in t:
    pos.append(item["upos"])

def merge(list1, list2):

    merged_list = []
    for i in range(max((len(list1), len(list2)))):

        while True:
            try:
                tup = (list1[i], list2[i])
            except IndexError:
                if len(list1) > len(list2):
                    list2.append('')
                    tup = (list1[i], list2[i])
                elif len(list1) < len(list2):
                    list1.append('')
                    tup = (list1[i], list2[i])
                continue

            merged_list.append(tup)
            break
    return merged_list

PosTuple=merge(pos, d)

for item1, item2 in PosTuple:
    p=Production(Nonterminal(str(item1)), [str(item2)])

CFGgrammar.append(p)


def sentenceparse(sent):
	rd_parser=nltk.RecursiveDescentParser(CFGgrammar)
	trees=rd_parser.parse(sent.split())
	treelist=list(trees)
	for tree in treelist:
		print(tree)
