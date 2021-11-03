from app import app,SQLAlchemy

db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nama = db.Column(db.String(50),nullable=False)

    def __repr__(self) -> str:
        return f'< nama : {self.nama} >'



