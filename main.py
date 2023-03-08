from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def preparation(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def job(prof):
    return render_template('training.html', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
