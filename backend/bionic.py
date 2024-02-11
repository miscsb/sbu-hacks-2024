import re

def is_word(word):
    return not not re.match(r'[a-zA-Z]+', word)

def make_bionic_word(word):
    mid = (1 + len(word)) // 2
    return '**' + word[0:mid] + '**' + word[mid:]

def make_bionic_line(line):
    if line.startswith('#'):
        return line
    else:
        return ' '.join(map(lambda item: (make_bionic_word(item) if is_word(item) else item), line.split()))
    
def make_bionic_content(text):
    lines = text.split('\n')
    lines = map(make_bionic_line, lines)
    return '\n'.join(lines)
