from string import punctuation
def most_common_words(filename: str, lower_limit: int):
    wstring = file_reader(filename)
    first_list = [(n, wstring.split().count(n)) for n in wstring.split() if wstring.split().count(n) >= lower_limit]
    return {n[0]: n[1] for n in first_list}


def file_reader(filename: str):
    x = ''
    with open(filename) as f:
        for line in f :
            x += line.translate(str.maketrans("","", punctuation))
    return x


