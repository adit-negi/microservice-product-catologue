from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@db/main'
CORS(app)

db = SQLAlchemy(app)



class FormAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    form_id = db.Column(db.Integer)
    question_id = db.Column(db.Integer)
    answer_text = db.Column(db.String(200))
    answer_key = db.Column(db.String(200))

    UniqueConstraint('form_id', 'question_id', name='form_user_unique')


@app.route('/')
def index():
    return 'Hello'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
