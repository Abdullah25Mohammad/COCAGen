import json
from collections import Counter

SENTENCEPATTERNSPATH = 'SentencePatterns/SentencePatterns.json'
OUTPATH = 'SentencePatterns/SentencePatterns_Common.json'

MINCOUNT = 40 # Minimum number of times a pattern must occur to be kept
MINLENGTH = 0 # Minimum length of a pattern to be kept
MAXLENGTH = 20 # Maximum length of a pattern to be kept

# Purpose of this program is to keep only the most common sentence patterns
# Note: Patterns are stored as lists

with open(SENTENCEPATTERNSPATH, 'r') as f:
    sentence_patterns = json.load(f)

# Count the frequency of each pattern
pattern_counts = Counter(map(tuple, sentence_patterns))

# Keep only the patterns that appear more than MINCOUNT times
common_patterns = [list(pattern) for pattern, count in pattern_counts.items() if count >= MINCOUNT]

# Keep only the patterns that are between MINLENGTH and MAXLENGTH
common_patterns = [pattern for pattern in common_patterns if len(pattern) >= MINLENGTH and len(pattern) <= MAXLENGTH]


OUTPATH = OUTPATH[:-5] + '_' + str(MINCOUNT) + '_' + str(MINLENGTH) + '-' + str(MAXLENGTH) + '.json'


with open(OUTPATH, 'w') as f:
    json.dump(common_patterns, f)


