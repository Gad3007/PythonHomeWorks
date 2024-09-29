

words = ['apple', 'banana', 'orange', 'apple', 'abc', 'bca', 'banana']
def count_words(words):
    dict_words = {}
    for word in words:
        if dict_words.get(word, 0):
            dict_words[word] += 1
        else:
            dict_words[word] = 1

    print(dict_words)


if __name__ == '__main__':
    count_words(words)