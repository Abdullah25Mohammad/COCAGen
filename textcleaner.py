def clean_string(inp_str):
    if len(inp_str) == 0: # Skip empty strings
        return ''
    
    inp_str = inp_str.lower()
    out_str = ''

    inp_str_list = inp_str.split(' ')

    for i in range(len(inp_str_list)):
        word = inp_str_list[i]
        

        word = word.replace('.', ' .')
        word = word.replace(',', ' ,')
        word = word.replace('!', ' !')
        word = word.replace('?', ' ?')
        word = word.replace(':', ' :')
        word = word.replace(';', ' ;')
        word = word.replace('(', ' (')
        word = word.replace(')', ' )')
        word = word.replace('[', ' [')
        word = word.replace(']', ' ]')
        word = word.replace('{', ' {')
        word = word.replace('}', ' }')
        word = word.replace('-', ' -')
        word = word.replace('_', ' _')
        word = word.replace('/', ' /')
        word = word.replace('\\', ' \\')
        word = word.replace('|', ' |')
        word = word.replace('"', ' "')
        
        out_str += word + ' '

    # Remove double spaces
    for i in range(10):
        inp_str = inp_str.replace('  ', ' ')

    # Remove spaces at the beginning and end of the string
    if inp_str[0] == ' ' and len(inp_str) == 0:
        inp_str = inp_str[1:]
    if inp_str[-1] == ' ' and len(inp_str) == 0:
        inp_str = inp_str[:-1]
    
    out_str = inp_str.strip()
    
    return out_str


PUNCTUATION = [".", ",", "!", "?", ":", ";", "(", ")", "[", "]", "{", "}", "-", "_", "/", "|", "\"", "'", "n't", "nt"] # n't is a special case
ENDPUNCTUATION = [".", "!", "?"]

def format_string(inp_list):
    if inp_list[0] in PUNCTUATION: # Remove the first word if it is punctuation
        inp_list = inp_list[1:]

    out = ''
    for i in range(len(inp_list)):
        word = inp_list[i]

        if i == 0 or inp_list[i-1] in ENDPUNCTUATION:
            word = word.capitalize()

        if word in PUNCTUATION:
            out += word
        else:
            out += ' ' + word

    
    return out.strip()
    

def clean_pos(pos):
    # Remove everything after '_'
    pos = pos.split('_')[0]

    # Remove @, %, $, and # symbols
    pos = pos.replace('@', '')
    pos = pos.replace('%', '')
    pos = pos.replace('$', '')
    pos = pos.replace('#', '')

    return pos