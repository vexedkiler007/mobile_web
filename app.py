from flask import Flask, render_template, url_for

app = Flask(__name__)

rules = ["If you want don't want to drink you drink",
         "If you eat ass you live fast"]


@app.route('/')
def hello_world():
    rules = [{'author': "vexed", "rule": "If you say no to a drink you drink", "num": 1},
             {'author': "cool", "rule": "If you open a drink then everyone drinks", "num": 2},
             {'author': "Dario", "rule": "If read this rule you drink", "num": 3},
             {'author': "Dario", "rule": "If read this rule you drink", "num": 3},
             {'author': "Dario", "rule": "If read this rule you drink", "num": 3},
             {'author': "Dario", "rule": "If read this rule you drink", "num": 3},
             {'author': "Dario", "rule": "If read this rule you drink", "num": 3},
             {'author': "Dario", "rule": "If read this rule you drink", "num": 3},
             ]
    return render_template('jinja_test.html', rules = rules)


if __name__ == '__main__':
    app.run()
