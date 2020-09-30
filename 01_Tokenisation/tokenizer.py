import sys, re

abbr = ['etc.', 'etj.', 'i.e.', 'e.g.', 'p. sh.', '(p. sh.', 'rr.', 'I. H. King.', 'c.', 'p. e. s', 'Xh. G.']

def tokenize(line, abbr):
    line = re.sub(r'([\(\)"?:!;])', r' \g<1> ', line)
    line = re.sub(r'([^0-9]),', r'\g<1> ,', line )
    line = re.sub(r', ([^0-9])', r' \g<1>', line)
    line = re.sub(r'  _', ' ', line[:-1])

    output = []
    for token in line.split(' '):
        if token=='':
            continue
        if token[-1] == '.' and token not in abbr:
            token = token[:-1] + ' .'
        output.append(token)

    return ' '.join(output)


line = sys.stdin.readline ()

while line != '':
    print (tokenize(ling.strip('\n'), abbr))
    line=sys.stdin.readline()

'''
When I run this code on my albanian text, it returns the "IndexError: string index out of range"
message that pertains to line 7. I inspected my wiki.txt file and noticed that there are several
empty lines or indented spaces that are not necessarily recognized "empty" but
some kind of an individual/independent line, and so the index [-1] does not exist
for these empty spaces, I guess. When I deleted some of these empty lines/spaces
the code seemed to be running, until it hits the next empty/not-empty one.

For future work, I would have to do a minimal processing of the text file
so that it does not contain these problematic lines/spaces.
'''

'''
Questions:
1. Why should we split punctuation from the token it goes with ?
--Because punctuation is not really a part of its preceding word.
In other words, should we really treat "word." and "word" separately?
Punctuation like "." "?" or "!" are usually more of a separate token
for sentence boundaries, phrasal boundaries, etc.

2. Should abbreviations with space in them be written as a single token or two tokens ?
--I believe abbreviations of names normally refer to one entity, so they should be
written as single tokens. Abbreviations such as e.g. or i.e. may be debatable, as the spellout
of them are usually multi words such as "exempli gratia" and "id est" or "for example" and "in other words"
This can be expanded to the question of whether we should treat phrasal verbs or idiomatic expressions
as one single token or not. I believe it is safe enough to treat them as a single token.
Consider, for example, Ph. D. Although it is an abbreviation with space in them, it may be more confusing
to treat it as two separate tokens in terms of syntactic and semantic analyses.

How about numerals like 134 000 ?
--For the similar reason, I think it would be less ambiguous if we treated this as a single token.

If you have a case suffix following punctuation, how should it be tokenised ?
--I think the case suffix should be tokensied along with the punctuation and its original head noun.,
as in reality it is attached to the head noun, not punctuation. Maybe the text can be annotated such
that it can preserve the linear order of punc-head noun-punc-suffix, but I believe the tokenization can ignore
if you are interested in doing morphological/syntactical analyses of a text. On the other hand, if you are
interested in looking at the distribution of punctionation or suffix markers, you might want to tokenize it as is,
so that you would see that the suffix marker immediately follows punctuation.

Should contractions and clitics be a single token or two (or more) tokens ?
-- This also depends on what you are trying to obtain from your analyses.
If you would want to compare the distribution of contractions and clitics versus their original expanded words, it may be
easier if you treat them as single tokens.
If you care less about such distribution but doing a simple syntactic analyses such as building treebanks, you might be better of
by separating and treating them as two tokens...

'''
