import string
import json
import os

TXTPATH = 'TXT'
OUTPATH = 'RWJSON'
    
printable = set(string.printable) # For filtering out non ASCII characters

# GET THE NEXT WORDS

def RWJSON(ref):
    out = dict()

    with open(ref, "r") as file:
        text = file.read()
        text = ''.join(filter(lambda x: x in printable, text)) # For filtering out non ASCII characters
        text = text.lower()

        words = text.split()

        for i in range(len(words)-1):
            word = words[i]
            if word not in out:
                out[word] = []

            nw = words[i+1]
            if nw not in out[word]:
                out[word].append(nw)
        
    return out


# ---------------------------------------------------------------------------------------

f_count = 0


for file in os.listdir(TXTPATH):
    f_count += 1

    print('Processing file {:10s}\t{:d} of {:d}'.format(file, f_count, len(os.listdir(TXTPATH))))

    if file.endswith('.txt'):
        out = RWJSON(TXTPATH + '/' + file)

        with open(OUTPATH + '/' + file[:-4] + '.json', 'w') as f:
            json.dump(out, f)

    