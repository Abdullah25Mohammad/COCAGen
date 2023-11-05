import json
import os

JSONFOLDERPATH = 'RWJSON'
OUTPATH = 'RWJSON_MERGED.json'

corpus = {}

f_count = 0

for file in os.listdir(JSONFOLDERPATH):
    f_count += 1

    print('Processing file {:10s}\t{:d} of {:d}'.format(file, f_count, len(os.listdir(JSONFOLDERPATH))))

    if file.endswith('.json'):
        with open(JSONFOLDERPATH + '/' + file, 'r') as f:
            data = json.load(f)

            for word in data:
                if word not in corpus:
                    corpus[word] = []

                corpus[word] += data[word]

                # REMOVE DUPLICATES

                corpus[word] = list(set(corpus[word]))


with open(OUTPATH, 'w') as f:
    json.dump(corpus, f)
