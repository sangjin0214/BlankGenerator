from flask import Flask, request
import sys
import blankGenerator
application = Flask(__name__, static_folder='static', static_url_path='')


@application.route("/textselect")
def select():
    form = ''
    form += '<p>지문 파일 제목을 입력해주세요 ex) jimun.txt</p><br>'
    form += '<form action="/" method="post">'
    form += '<input type="text" name="title">'
    form += '<input type="submit" value="제출">'
    form += '</form>'
    return form

@application.route("/", methods=['POST'])
def test():
    title = request.form['title']
    test, answer = blankGenerator.process(title)
    exp = ['!', '@', '#', '$', '.', ',', '-', '&', '(', ')', '*', '?', ';', ':', '"', "'"]
    test_form = ''
    test_form += '<p>문제</p><br>'
    test_form += '<form action="/answer" method="post">'
    num = 0
    n = 1
    for text in test:
        test_form += str(n) + '번 지문<br>'
        for word in text:
            if word == '':
                test_form += ' <input type="text" name="test' + str(num) + '">'
                num += 1
            else:
                if word in exp:
                    test_form += word
                else:
                    test_form += ' ' + word
        n += 1
        test_form += '<br><br><br>'
    test_form += '<input type="hidden" name="num" value="' + str(num-1) + '"><br>'
    num = 0
    for temp in answer:
        test_form += '<input type="hidden" name="n' + str(num) + '" value="' + temp + '">'
        num += 1
    test_form += '<input type="hidden" name="n" value="' + str(num-1) + '">'
    test_form += '<input type="submit" value="제출">'
    test_form += '</form>'
    return test_form


@application.route("/answer", methods=['POST'])
def answer():
    test_form = ''
    test_form += '<p>결과</p><br><br>'
    num = request.form['num']
    n = request.form['n']
    ans = []
    answer = []
    i = 0
    while True:
        answer.append(request.form['n' + str(i)])
        if i == int(n):
            break
        i += 1
    i = 0
    while True:
        ans.append(request.form['test' + str(i)])
        if i == int(num):
            break
        i += 1
    n = 0
    m = ''
    for m in answer:
        if m != ans[n]:
            test_form += str(n+1) + '. ' + ans[n] + ' -> ' + m + '<br>'
        else:
            test_form += str(n+1) + '. Correct<br>'
        n += 1
    return test_form


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=int(sys.argv[1]))
