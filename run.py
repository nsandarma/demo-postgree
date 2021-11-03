from enum import unique
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import os

database = 'postgres://tsbmlqwxkzbkoh:32f18c20a20469a1c96fef9168018ad84786825afc39ec57e08148497682ebb5@ec2-54-159-35-35.compute-1.amazonaws.com:5432/d1ru9t99pvgmmb'
sqlite = 'sqlite:///test.db'
secret = 'fasisme123'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database
app.config['SECRET_KEY'] = secret
db = SQLAlchemy(app)

class Siswa(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nama = db.Column(db.String,unique=True)

    def __repr__(self) -> str:
        return f'<nama {self.nama}>'

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        nama = request.form['nama']
        if nama:
            q = Siswa(nama=nama)
            db.session.add(q)
            db.session.commit()
    data = Siswa.query.all()
    return render_template('index.html',data=data)

@app.route('/delete/<int:id>')
def delete(id):
    try:
        q = Siswa.query.filter_by(id=id).first()
        db.session.delete(id)
        db.session.commit()
    except Exception as e:
        return "salah"

if __name__ == '__main__':
    app.run(debug=True)
            
