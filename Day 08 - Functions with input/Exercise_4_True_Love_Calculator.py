def true_word_count(name):
    cntTrue = 0
    for letter in name:
        if letter == 'T' or letter == 't':
            cntTrue += 1
        elif letter == 'R' or letter == 'r':
            cntTrue += 1
        elif letter == 'U' or letter == 'u':
            cntTrue += 1
        elif letter == 'E' or letter == 'e':
            cntTrue += 1
    return cntTrue


def love_word_count(name):
    cntLove = 0
    for letter in name:
        if letter == 'L' or letter == 'l':
            cntLove += 1
        if letter == 'O' or letter == 'o':
            cntLove += 1
        if letter == 'V' or letter == 'v':
            cntLove += 1
        if letter == 'E' or letter == 'e':
            cntLove += 1
    return cntLove


def calculate_love_score(name1, name2):
    names = name1 + name2
    total_TrueWordCnt = true_word_count(names)
    total_LoveWordCnt = love_word_count(names)
    print(f"{total_TrueWordCnt}{total_LoveWordCnt}")


calculate_love_score("Angela Yu", "Jack Bauer")
calculate_love_score("Kanye West", "Kim Kardashian")