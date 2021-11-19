import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///db.sqlite")
db = SQLAlchemy(app)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=False)
    text = db.Column(db.String, unique=False)


db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/omeni', methods=['GET', 'POST'])
def omeni():
    if request.method == 'GET':
        return render_template('omeni.html')
    elif request.method == 'POST':
        email = request.form.get('email')
        message = request.form.get('message')

        print(email + ' ' + message)
        msg = Message(email=email, text=message)
        db.session.add(msg)
        db.session.commit()

        return render_template('omeni.html', alert="message received and saved")


if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
