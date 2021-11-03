from enum import unique
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

class Siswa(db.Model):
    __tablename__ = 'siswa'
    id = db.Column(db.Integer,primary_key=True)
    nama = db.Column(db.String,unique=True)

db.init_app()
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
            
