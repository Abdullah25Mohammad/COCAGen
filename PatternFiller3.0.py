import json
import random
from textcleaner import format_string, clean_pos

POSTAGSPATH = 'pos_tags.json'

SENTENCEPATTERNSPATH = 'SentencePatterns/SentencePatterns_Common_15_5-20.json'
VOCABPATH = 'Vocab/Vocab_noduplicates_nodashes.json'
RWJSONPATH = 'RWJSON_MERGED.json'

SAVETODOC = True
OUTDOCPATH = 'GeneratedSentences/_Common_15_5-20_nodashes.txt'


SENTCOUNT = 100

with open(SENTENCEPATTERNSPATH, 'r') as f:
    sentence_patterns = json.load(f)

with open(POSTAGSPATH, 'r') as f:
    pos_tags = json.load(f)

with open(VOCABPATH, 'r') as f:
    vocab = json.load(f)

with open(RWJSONPATH, 'r') as f:
    rwjson = json.load(f)


def choose_next_word(pos, prev_word=None, vocab=vocab, rwjson=rwjson):
    if prev_word == None:
        return random.choice(vocab[pos]) # If no previous word, just choose a random word from the vocab
    
    if pos not in vocab or prev_word not in rwjson: # To avoid key errors
        return random.choice(vocab[pos])
    
    vocab_words = vocab[pos]
    possible_nw = []

    for w in vocab_words:
        if w in rwjson[prev_word]:
            possible_nw.append(w)

    # If there are no possible next words, just choose a random word from the vocab
    if len(possible_nw) == 0:
        return random.choice(vocab[pos])
    
    
    
    return random.choice(possible_nw)


def fill_pattern(pattern, vocab):

    out = []
    for pos in pattern:
        word = ''
        if len(out) > 0:
            prev_word = out[-1]
        else:
            prev_word = None

        if pos not in vocab:
            pos = clean_pos(pos) # Clean pos then check again
            
            if pos not in vocab:
                word = '[unknown]'
            else:
                word = choose_next_word(pos, prev_word, vocab, rwjson)
        else:
            word = choose_next_word(pos, prev_word, vocab, rwjson)
            


        out.append(word)

    return out





saved_sent_count = 0
while saved_sent_count < SENTCOUNT:
    p = random.choice(sentence_patterns)

    if len(p) < 5:
        continue

    filled_sent = fill_pattern(p, vocab)
    filled_sent = format_string(filled_sent)


    if not SAVETODOC:
        print(filled_sent)
    else:
        saved_sent_count += 1
        with open(OUTDOCPATH, 'a') as f:
            f.write(filled_sent + '\n')
            print("Saved {:d} sentences so far".format(saved_sent_count))
    

    
