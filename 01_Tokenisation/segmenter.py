import sys

line = sys.stdin.readline ()

while line != '':
    for token in line.split(' '):
        if token[-1] in '!?':
            sys.stdout.write(token + '\n')
        elif token[-1] == '.':
            if token in ['etc.', 'i.e.', 'e.g.', 'p. sh.', '(p. sh.', 'rr.', 'I. H. King.', 'c.', 'p. e. s', 'Xh. G.'] :
                sys.stdout.write(token + ' ')
            else:
                sys.stdout.write(token + '\n')
        else:
            sys.stdout.write (token + ' ')
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
How should you segment sentences with semi-colon? As a single sentence or as two sentences? Should it depend on context?
-- I guess the safest bet is to make judgements depending on context, and the whole judgement can even expand to the treatment
of coordinated sentence like this. If you strictly abide by the assumption that .,?, ! are the most prominent sentence breaker,
then the sentences with semi-colons should not be treated as a separate sentence.
On the other hand, such sentences should absolutely be treated as separate sentence, if a "sentence" means a finite CP (that's not subordinate, probably) to you.
Therefore, I believe that this actually depends on your theoretical background and what you are looking to obtain from the data.

Should sentences with ellipsis... be treated as a single sentence or as several sentences?
--Also depends on whether you believe in the deletion theory or copying theory (Can't recall the correct names...)
Regardless of the theory, though, I believe most people would naturally parse ellipses as one sentence, and I don't think
it is not wrong to segment the sentences according to people's common judgment rather than linguistic theories.

If there is an exclamation after the first word in the sentence should it be a separate sentence? How about if there is a comma?
Can you think of some hard tasks for the segmenter?
If you were to distinguish sentences like "Oh! This is so hard!" and "Oh, this is so hard!", I believe there is nearly zero semantic difference.
I think most of the word processors and English teacher would count the first instance as two sentences and the latter as one., strictly judging by
punctuation rules. Also, there are sentences that only contain one word -- mostly imperative sentences such as "go!" "out!"

Some of the hard task would be cases in which the name of an entity alrady contains "!" such as Yahoo!.
Here the exclamation doesn't really work as a sentence boundary. Similarly, if you were to process a mathmatics paper and come accross
something like "5! is 120.", ! is also not punctuation.
'''
