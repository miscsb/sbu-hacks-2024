def make_bionic_paragraph(text):
    words = text.split(' ')
    return ' '.join(map(make_bionic_word, words))

def make_bionic_word(word):
    mid = (1 + len(word)) // 2
    return '<b>' + word[0:mid] + '</b>' + word[mid:]
    