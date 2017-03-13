import flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from genq import genqs
app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'Hard@to#guess^and!long%enough.'


@app.route('/')
def index():
    questions = genqs(20,20,['+','-'])
    return flask.render_template('questions.html', questions=questions)

@app.route('/check')
def check():
    pass

if __name__ == '__main__':
    app.run(debug=True)
