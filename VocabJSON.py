import json
import os
from textcleaner import clean_string

INFOLDERPATH = 'CorpusRawTXT'
OUTPATH = 'Vocab/Vocab.json'

ENDING_PUNCTUATION = ['.', '!', '?', '"']

corpus = {}
f_count = 0

REMOVEDUPLICATES = False
REMOVEDASHES = True

for file in os.listdir(INFOLDERPATH):
    with open(INFOLDERPATH + '/' + file, 'r', encoding='latin-1') as f:
        text = f.read()
    
    f_count += 1
    
    print('Processing file {:10s}   {:d} of {:d}'.format(file, f_count, len(os.listdir(INFOLDERPATH))))

    text = text.split('\n')

    cs_pattern = [] # Current Sentence Pattern

    # Read each line (word) one by one
    for i in range(len(text)):
        if i % 100000 == 0:
            print('Processing line {:10d} of {:10d}'.format(i, len(text)))

        line = text[i]

        line = clean_string(line)

        # Line is in format:
        # TextID \t word \t lemma \t POS

        line = line.split('\t')

        if len(line) < 4:
            continue

        line = [clean_string(x) for x in line]

        text_id = line[0]
        word = line[1]
        lemma = line[2]
        pos = line[3]

        # If any of the fields are empty, skip this line
        if len(text_id) == 0 or len(word) == 0 or len(lemma) == 0 or len(pos) == 0:
            continue

        # If any words or lemmas are whitespace, skip this line
        if word.isspace() or lemma.isspace():
            continue

        # If the word contains dashes, skip this line
        if REMOVEDASHES and word.__contains__('-'):
            continue

        if pos not in corpus:
            corpus[pos] = []
        
        if REMOVEDUPLICATES:
            if lemma not in corpus[pos]:
                corpus[pos].append(lemma)
        else:
            corpus[pos].append(lemma)


if REMOVEDUPLICATES:
    OUTPATH = OUTPATH[:-5] + '_noduplicates.json'

if REMOVEDASHES:
    OUTPATH = OUTPATH[:-5] + '_nodashes.json'

# Save corpus to file
with open(OUTPATH, 'w') as f:
    json.dump(corpus, f)