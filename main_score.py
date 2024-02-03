from flask import Flask, render_template
import requests
import utils

app = Flask(__name__)


def response():
    request = requests.get("http://127.0.0.1:20000/")
    return request


@app.route('/score')
def openfile():
    try:
        scores_file = open(utils.scores_file_name, 'r', encoding='UTF-8')
        score = scores_file.read()
        scores_file.close()
        return render_template('score.html', SCORE=score)
    except Exception as error:
        return render_template('error.html', ERROR=error)


if __name__ == "__main__":
    app.run(port=20000)
