import sys
from conllu import parse


#Extracting dictionary from the conllu file provided in UD_Japanese

sentences=parse(open('/Users/sykim/LING-L545/UD_Japanese-GSD-master/ja_gsd-ud-train.conllu').read())
t=[]
for sentence in sentences:
    for tokens in sentence:
        t.append(tokens)
d=[]
for item in t:
    d.append(item["form"])


#MaxMatch that can read sentences and compare with the dictionary.
def MaxMatch(s, d):
    index = 0
    res = []
    size = len(max(d, key=len))
    while index < len(s):
        word = None
        for i in range(size, 0, -1):
            if index + i > len(s):
                continue
            else:
                pieces = s[index: index+i]
                if pieces in d:
                    word = pieces
                    res.append(word)
                    index += i
                    break
        if word is None:
            res.append(s[index])
            index += 1
    return res

if __name__ == "__main__":

    #d = open(filename).read()

    s = sys.stdin.readline ()

    for item in MaxMatch(s, d):
        print(item + '\n' )
        line = sys.stdin.readline ()
