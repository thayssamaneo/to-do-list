from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class lista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tarefa = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(150), nullable=False)
    prioridade = db.Column(db.String, nullable=False)
    concluido = db.Column(db.Boolean, default=False)

    __tablename__ = 'listaDeTarefas'