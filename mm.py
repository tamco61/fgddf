from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/galery', methods=['POST', 'GET'])
def odd_even():
    if request.method == 'GET':
        os.chdir('static/img')
        lst = os.listdir()
        os.chdir('../../')
        return render_template('galery.html', title='Красная планета', lst=lst)
    elif request.method == 'POST':
        f = request.files['file']
        os.chdir('static/img')
        lst = os.listdir()
        os.chdir('../../')
        if str(f) != "<FileStorage: '' ('application/octet-stream')>":
            for i in range(1, 1000):
                if 'mars' + str(i) + '.jpg' not in lst:
                    f.save(f'static/img/mars{str(i)}.jpg')
                    break
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')