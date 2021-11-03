from werkzeug.utils import redirect
from app import app,render_template,request
from .models import db,Data

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == "POST":
        nama = request.form['nama']
        if nama:
            data = Data(nama=nama)
            db.session.add(data)
            db.session.commit()
    query = Data.query.all()
    return render_template('index.html',data=query)
@app.route('/delete/<int:id>')
def delete(id):
    try:
        d = Data.query.filter_by(id=id).first()
        db.session.delete(d)
        db.session.commit()
    except Exception as e:
        return "salah"
    return redirect('/')
