from flask import Flask, render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db=SQLAlchemy(app)
class Super(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(200),nullable=False)
    sexo=db.Column(db.String(2),nullable=False)

    def __repr__(self):
        return '<Super %r>' %self.id
#WHEN  we do this we have to go to the terminal and then import the name of the
#archive and import the name that we put db example from CRUDSuper import db and then we have to 
#make the db.create_all()
#With this instruction the database is created
@app.route('/',methods=['POST','GET'])
def Index():
    if request.method=='POST':
        Super_nombre=request.form['nombre']
        Super_sexo=request.form['sexo']
        new_Super=Super(nombre=Super_nombre,sexo=Super_sexo)
        try:
            db.session.add(new_Super)
            db.session.commit()
            return redirect('/')
        except:
            return 'Hubo un error'
    else:
        supers=Super.query.order_by(Super.id).all()
        return render_template('Index.html',supers=supers)
@app.route('/delete/<int:id>')
def delete(id):
    superdel=Super.query.get_or_404(id)
    try:
        db.session.delete(superdel)
        db.session.commit()
        return redirect('/')
    except:
        return 'No se a podido eliminar'
@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    superh=Super.query.get_or_404(id)
    if request.method=='POST':
        superh.nombre=request.form['nombre']
        superh.sexo=request.form['sexo']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'Hubo un problema'
    else:
        return render_template('update.html',superh=superh)

if __name__ == "__main__":
    app.run(debug=True)
