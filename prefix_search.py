from typing import List, Tuple


# with open('file.txt', 'r', encoding='utf-8') as f:
#     word_list = [word.strip() for word in f.readlines()]
#
# print(word_list)


def bruteforce(word_list: List[str]) -> Tuple[int, Tuple[str, str]]:
    """Brute force solution"""
    best = 0
    best_pair = None
    for i in range(len(word_list)):
        for j in range(len(word_list)):
            if word_list[i] != word_list[j]:
                for l in range(min(len(word_list[i]), len(word_list[j])), 0, -1):
                    if word_list[i][-l:] == word_list[j][:l]:
                        if l > best:
                            best = l
                            best_pair = (word_list[i], word_list[j])
    return best, best_pair


def dict_find(word_list: List[str]) -> Tuple[int, Tuple[str, str]]:
    """Dictionary finding solution"""
    prefix = dict()
    best = 0
    best_pair = None
    for word in word_list:
        for l in range(1, len(word) + 1):
            if word[:l] not in prefix:
                prefix[word[:l]] = {word:''}
            else:
                prefix[word[:l]][word] = ''

    for word in word_list:
        for l in range(len(word), 0, -1):
            suf = word[-l:]
            if suf in prefix:
                for second_word in prefix[suf]:
                    if second_word != word:
                        if l > best:
                            best = l
                            best_pair = (word, second_word)
    return best, best_pair

