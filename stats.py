def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words_list = text.split()
    return len(words_list)


def get_count_perletter(text):
    letter_set = {
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    }
    letter_dic = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }
    lower_case_text = text.lower()
    for letter in lower_case_text:
        if letter in letter_set:
            letter_dic[letter] += 1
    return letter_dic


def give_numbs(each_dir):
    return each_dir["nums"]


def sort_letter_count(dir):
    list_of_dir = []
    for key in dir:
        dir_labelled = {"letter": key, "nums": dir[key]}
        list_of_dir.append(dir_labelled)
    list_of_dir.sort(key=give_numbs, reverse=True)
    return list_of_dir
