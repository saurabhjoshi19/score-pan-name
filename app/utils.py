import numpy as np


# from difflib import SequenceMatcher


def levenshtein_ratio(s, t):
    rows = len(s) + 1
    cols = len(t) + 1
    distance = np.zeros((rows, cols), dtype=int)
    for i in range(1, rows):
        for j in range(1, cols):
            distance[i][0] = i
            distance[0][j] = j

    for col in range(1, cols):
        for row in range(1, rows):
            if s[row - 1] == t[col - 1]:
                cost = 0
            else:
                cost = 1
            distance[row][col] = min(distance[row - 1][col] + 1,
                                     distance[row][col - 1] + 1,
                                     distance[row - 1][col - 1] + cost)

    ratio = ((len(s) + len(t)) - distance[row][col]) / (len(s) + len(t)) * 100
    return round(ratio, 2)


'''
words = ['saurabh joshi', 'j saurabh', 'joshi saurabh', 'sourabh joshi', 'sourav joshi']

test_word = 'saurabh joshi'

for word in words:
    print('Levenshtein Distance', levenshtein_ratio(test_word, word))
    print('Sequence Matcher', SequenceMatcher(None, test_word, word).ratio())
'''
