from api import db 

class aluno(db.Model):
    __tablename__ = "aluno"
    id = db.Collumn(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Collumn(db.String(100), nullable=False)
    data_nascimento = db.Collumn(db.Date, nullable=False)