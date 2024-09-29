

def del_rep_chars(text):
    empty_string = ""
    list1 = [text[0]]
    if text == empty_string:
        return text
    for i in range(1, len(text)):
        if text[i] != text[i-1]:
            list1.append(text[i])
    res = ''.join(list1)
    print(res)

if __name__ == '__main__':
    text = input("Введите текст: ")
    del_rep_chars(text)
