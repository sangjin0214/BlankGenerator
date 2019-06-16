from random import randint


def process(title):
    n = 0
    temp = ""
    text = []
    exp = ['!', '@', '#', '$', '.', ',', '-', '&', '(', ')', '*', '?', ';', ':', '"', "'"]
    answer = []
    f = open("./questions/" + title, "r")
    for line in f.readlines():
        for e in exp:
            line = line.replace(e, ' ' + e + ' ') if e in line else line
        line = line.replace('\xad', '-')
        if n != 0:
            temp += line
        n += 1
        if line == "\n":
            text.append(temp)
            temp = ""
            n = 0
    splitted_txt = []
    splitted_text = []
    for txt in text:
        for word in txt.split():
            splitted_txt.append(word)
        splitted_text.append(splitted_txt)
        splitted_txt = []
    q = 0
    for splitted_txt in splitted_text:
        for word in splitted_txt:
            if word == '':
                q += 1
    n = 0
    m = 0
    for splitted_txt in splitted_text:
        for word in splitted_txt:
            if randint(1, 100) <= 30 and word not in exp:
                answer.append(word)
                splitted_text[m][n] = ''
            n += 1
        n = 0
        m += 1
    q = 0
    for splitted_txt in splitted_text:
        for word in splitted_txt:
            if word == '':
                q += 1
    return splitted_text, answer
